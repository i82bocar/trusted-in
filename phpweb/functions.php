<?php
// GLOBAL TIME
$tm = date("Y-m-d H:i:s");

// Essential functions
include __DIR__ .'/sd_timeline_media_generator.php';
include __DIR__ .'/sd_mailer.php';

// Classify file extensions
$imageExtensions = array('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp');
$videoExtensions = array('mp4', 'webm', '3gp');
$audioExtensions = array('mp3', 'wav', 'ogg', 'flac');
$documentExtensions = array('pdf', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'txt');
$archiveExtensions = array('zip', 'rar', 'tar', 'gz', 'x-zip-compressed');
$dataExtensions = array('csv', 'xml');
$vectorExtensions = array('svg', 'svg+xml');

/**
 * Generate a random string, using a cryptographically secure
 * pseudorandom number generator (random_int)
 *
 * This function uses type hints now (PHP 7+ only), but it was originally
 * written for PHP 5 as well.
 *
 * For PHP 7, random_int is a PHP core function
 * For PHP 5.x, depends on https://github.com/paragonie/random_compat
 *
 * @param int $length      How many characters do we want?
 * @param string $keyspace A string of all possible characters
 *                         to select from
 * @return string
 */
function random_str(
    int $length = 64,
    string $keyspace = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
): string {
    if ($length < 1) {
        throw new \RangeException("Length must be a positive integer");
    }
    $pieces = [];
    $max = mb_strlen($keyspace, '8bit') - 1;
    for ($i = 0; $i < $length; ++$i) {
        $pieces []= $keyspace[random_int(0, $max)];
    }
    return implode('', $pieces);
}

$a = random_str(32);
$b = random_str(8, 'abcdefghijklmnopqrstuvwxyz');
$c = random_str(8);

// Strings
function startsWith($haystack, $needle)
{
     $length = strlen($needle);
     return (substr($haystack, 0, $length) === $needle);
}

function endsWith($haystack, $needle)
{
    $length = strlen($needle);
    if ($length == 0) {
        return true;
    }

    return (substr($haystack, -$length) === $needle);
}

// /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Compress image
function compressImage($fileTmpName, $fileDestination, $quality) {

    $info = getimagesize($fileTmpName);

    if ($info['mime'] == 'image/jpeg')
        $image = imagecreatefromjpeg($fileTmpName);

    elseif ($info['mime'] == 'image/gif')
        $image = imagecreatefromgif($fileTmpName);

    elseif ($info['mime'] == 'image/png')
        $image = imagecreatefrompng($fileTmpName);

    elseif ($info['mime'] == 'image/webp')
        $image = imagecreatefromwebp($fileTmpName);
    
    else
        return false;

  imagejpeg($image, $fileDestination, $quality);

};

//
function view_prof_link($link, $con)
{
    $query = "SELECT * FROM `user_log_inf` WHERE `profile_link`='".$link."'";
    $result = mysqli_query($con, $query);

    if ($row = mysqli_fetch_assoc($result)) {
        return "true";
    }else{
        return "false";
    }

}

// Get user ip
function getUserIpAddr(){
    if(!empty($_SERVER['HTTP_CLIENT_IP'])){
        //ip from share internet
        $ip = $_SERVER['HTTP_CLIENT_IP'];
    }elseif(!empty($_SERVER['HTTP_X_FORWARDED_FOR'])){
        //ip pass from proxy
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    }else{
        $ip = $_SERVER['REMOTE_ADDR'];
    }
    return $ip;
}

//
function generate_profile_link($email)
{
    global $con;

    $email_us_name = (explode('@', $email)[0]);

    $new_prof_link = $email_us_name;

    while (view_prof_link($new_prof_link, $con) == "true") {
        $new_prof_link = $email_us_name.".".random_str(4, 'abcdefghijklmnopqrstuvwxyz');
    }

    return $new_prof_link;

}

//
function make_search_phrase($phrase)
{
    $search_phrase = "";

    if (isset($phrase)) {

        $search_phrase = metaphone($phrase);
    }

    return $search_phrase;
}

// get cat name from id
function get_cat_name($cat_id)
{
    global $con;

    $query = "SELECT * FROM `sd_works_categories` WHERE `sd_work_cat_id` = '".$cat_id."'";

    $result = mysqli_query($con, $query);

    if ($row = mysqli_fetch_assoc($result)) {
        $work_cat_name = $row['sd_work_cat_name'];
    }else{
        $work_cat_name = "";
    }

    return $work_cat_name;
}

function isEmailVerified($email)
{
    global $con;

    // Check if there are any rows for the provided email
    $checkRowsSql = "SELECT * FROM sd_account_verification WHERE user_email = '$email'";
    $checkRowsResult = mysqli_query($con, $checkRowsSql);

    // If there are rows for the provided email
    if (mysqli_num_rows($checkRowsResult) > 0) {
        // Check if there are no unverified and not expired rows
        $verifySql = "SELECT * FROM sd_account_verification WHERE user_email = '$email' AND used = 0 AND email_verified = 0";
        $verifyResult = mysqli_query($con, $verifySql);

        // If there are no unverified and not expired rows, return true (Email is verified)
        if (mysqli_num_rows($verifyResult) == 0) {
            return true;
        }
    }

    // If no rows or there are unverified rows, return false (Email is not verified)
    return false;
}



function startEmailVerification($email)
{
    if (isEmailVerified($email) && !isset($_POST['ignore_verified'])){
        return;
    }

    global $con, $dbh;

    // Check if there is an unused verification record for the provided email
    $checkSql = "SELECT id FROM sd_account_verification WHERE user_email = :user_email AND used = 0 AND email_verified = 0 AND expiration_time > NOW()";
    $checkQuery = $dbh->prepare($checkSql);
    $checkQuery->bindParam(':user_email', $email, PDO::PARAM_STR);
    $checkQuery->execute();

    if ($checkQuery->rowCount() == 0) {
        // Generate a unique token 
        $c = random_str(4);
        $plain_token = viewSdAccVerifTokenKey($c);
		$token = base64_encode(maskData($plain_token));

        // Set the expiration time (adjust this as needed)
        // Get the current date and time
        $dt = new DateTime();
        // Add 20 minutes
        $dt->add(new DateInterval('PT20M'));

        // Format the date and time as a string
        $expirationTime = $dt->format("Y-m-d H:i:s");

        // Insert a new verification record
        $insertSql = "INSERT INTO sd_account_verification (user_email, token, expiration_time, used, created_at) VALUES (:user_email, :token, :expiration_time, 0, NOW())";
        $insertQuery = $dbh->prepare($insertSql);
        $insertQuery->bindParam(':user_email', $email, PDO::PARAM_STR);
        $insertQuery->bindParam(':token', $token, PDO::PARAM_STR);
        $insertQuery->bindParam(':expiration_time', $expirationTime, PDO::PARAM_STR);
        $insertQuery->execute();

        // Send the verification email with the generated token
        sendEmailVerificationEmail(unMaskData(base64_decode($email)), $token);
    }
}

function viewSdAccVerifTokenKey($c)
{
    global $con;

    $en_c = base64_encode(maskData($c));

    $query = "SELECT * FROM `sd_account_verification` WHERE `token` = '".$en_c."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result) || empty($c)) {
        generateUniqueSdAccVerifTokenKey();

    }else{
        return $c;
    }
}

function generateUniqueSdAccVerifTokenKey()
{
    $c = random_str(4);
    viewSdAccVerifTokenKey($c);
}

function get_cat_id($cat_name)
{
    global $con, $dbh;

    $query = "SELECT * FROM `sd_works_categories` WHERE `sd_work_cat_name` = '".$cat_name."'";

    $result = mysqli_query($con, $query);

    if ($row = mysqli_fetch_assoc($result)) {

    }else{
        $sql = "INSERT INTO `sd_works_categories`(`sd_work_cat_id`, `sd_work_cat_name`) VALUES (NULL, :sd_work_cat_name)";

        $query = $dbh->prepare($sql);

        $query->bindParam('sd_work_cat_name', $cat_name, PDO::PARAM_STR );

        $query->execute();
    }

    $query = "SELECT * FROM `sd_works_categories` WHERE `sd_work_cat_name` = '".$cat_name."'";

    $result = mysqli_query($con, $query);

    if ($row = mysqli_fetch_assoc($result)) {
        $cat_id = $row['sd_work_cat_id'];
    }else{
        $cat_id = 0;
    }

    return $cat_id;
}

//
function relative_date($relative_date)
{
    // Get the current time
    $current_time = time();

    // Convert the relative date to a timestamp
    $relative_time = strtotime($relative_date);

    // Calculate the difference in seconds
    $diff = $current_time - $relative_time;

    // echo($current_time ." ". $relative_time);
    // Determine the appropriate time unit
    if ($diff < 60) {
        // Seconds
        $relative_short_date = $diff;
        $ext = $relative_short_date > 1 ? 'Seconds' : 'Second';
    } elseif ($diff < 3600) {
        // Minutes
        $relative_short_date = floor($diff / 60);
        $ext = $relative_short_date > 1 ? 'Minutes' : 'Minute';
    } elseif ($diff < 86400) {
        // Hours
        $relative_short_date = floor($diff / 3600);
        $ext = $relative_short_date > 1 ? 'Hours' : 'Hour';
    } elseif ($diff < 2592000) {
        // Days
        $relative_short_date = floor($diff / 86400);
        $ext = $relative_short_date > 1 ? 'Days' : 'Day';
    } elseif ($diff < 31536000) {
        // Months
        $relative_short_date = floor($diff / 2592000);
        $ext = $relative_short_date > 1 ? 'Months' : 'Month';
    } else {
        // Years
        $relative_short_date = floor($diff / 31536000);
        $ext = $relative_short_date > 1 ? 'Years' : 'Year';
    }

    return $relative_short_date . " " . $ext;
}


function get_profile_details($email)
{
    global $con;

    $query = "SELECT * FROM `user_log_inf` WHERE `email_address`='".$email."' OR `profile_link`='".$email."'";

    $result = mysqli_query($con, $query);

    if ($row_profile = mysqli_fetch_assoc($result)) {
        if (empty($row_profile['profile_link'])) {

            $profile_link = generate_profile_link($row_profile['email_address']);

            $sql4 = "UPDATE `user_log_inf` SET  `profile_link`='".$profile_link."' WHERE `email_address`='".$row_profile['email_address']."'";

            $result4 = mysqli_query($con, $sql4);

            $row_profile['profile_link'] = $profile_link;

        }

    }else{
        $row_profile['user_id'] = "";
        $row_profile['first_name'] = "Unknown";
        $row_profile['second_name'] = "Account";
        $row_profile['email_address'] = "";
        $row_profile['phone_number'] = "";
        $row_profile['login_key'] = "";
        $row_profile['date_registered'] = "";
        $row_profile['prof_pic'] = "";
        $row_profile['cover_pic'] = "";
        $row_profile['profile_link'] = "";
        $row_profile['bio'] = "";
        $row_profile['other_links'] = "";
    }

    $prof_pic = base64_decode(unMaskData($row_profile['prof_pic']));
    $prof_cover = base64_decode(unMaskData($row_profile['cover_pic']));

    if (empty($prof_pic) || $prof_pic == "updaters/") {
        $row_profile['prof_pic'] = base64_encode(maskData("img/default/user.png"));
    }
    if (empty($prof_cover) || $prof_cover == "updaters/") {
        $row_profile['cover_pic'] = base64_encode(maskData(get_random_cover_pic()));
    }

    return $row_profile;
}

//
function get_sd_work_details($sd_work_id)
{
    global $my_email, 
    $con, 
    $tm,
    $imageExtensions,
    $videoExtensions,
    $audioExtensions,
    $documentExtensions,
    $archiveExtensions,
    $dataExtensions,
    $vectorExtensions;

    // Initialize empty values
    $uniq_work_id = "";
    $ttl = "";
    $desc = "";
    $post_date = "";
    $ext_link = "";
    $type = "";
    $likes = 0;
    $total_comments = 0;
    $views = 0;
    $cat_name = "";
    $demo_vids = "";
    $demo_imgs = "";
    $name = "";
    $prof_pic = "";
    $prof_link = "";
    $liked = false;
    $owner = false;
    $thumb = "";
    $cat_id = 0;

    $demo_vid_count = 0;
    $demo_imgs_count = 0;
    $files_count = 0;
    $demo_imgs = [];
    $demo_vids = [];
    $attached_files = [];

    $masked_id = base64_encode(maskData($sd_work_id));

    $query = "SELECT * FROM `sd_works` WHERE `sd_work_id` = '".$sd_work_id."' OR `sd_unique_work_id` = '".$sd_work_id."' OR `sd_unique_work_id` = '".$masked_id."'";
    $result = mysqli_query($con, $query);
    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
        $sd_unique_work_id = unMaskData(base64_decode($row['sd_unique_work_id']));
        
        $total_comments = getTotalCommentsByPostId($row['sd_unique_work_id']);

        if (getMyLike(base64_encode(maskData($row['sd_work_id'])))) {
            $liked = true;
        }

        if (isset($_SESSION['spinn_design_user'])) {
            if ($_SESSION['spinn_design_user'] == $row['sd_work_owner']) {
                $owner = true;
            }
        }

        if (!empty(unMaskData(base64_decode($row['sd_work_thumb'])))){
            $fileExt = explode('.', unMaskData(base64_decode($row['sd_work_thumb'])));
            $fileActualExt = strtolower(end($fileExt));
            if (in_array($fileActualExt, $imageExtensions)) {
                $thumb = unMaskData(base64_decode($row['sd_work_thumb']));
                // $thumb = str_replace('SP_DES', "compressed_SP_DES", $thumb);
                // replace ../
                $thumb = str_replace('../', "", $thumb);
                // check if thumb exists
                if(!empty($thumb)){
                    if (!file_exists($thumb) && !file_exists("../".$thumb)) {
                        $thumb = "";
                    }
                }else{
                    $thumb = "";
                }
            }
        }else{
            $thumb = "";
        }

        $cat_id = unMaskData(base64_decode($row['sd_work_cat']));
        $cat_name = unMaskData(base64_decode(get_cat_name($cat_id)));
        $dwn = get_download_permission($row['sd_unique_work_id']);

        $work_demos = unMaskData(base64_decode($row['sd_work_demos']));
        $work_demos = explode('XSPDX', $work_demos);
        
        for ($i=0; $i < count($work_demos); $i++) {
            if (!empty($work_demos[$i])) {
                $ext = explode('.', $work_demos[$i]);
                $ext = strtolower(end($ext));
                if (in_array($ext, $imageExtensions)) {
                    $work_demos[$i]= str_replace('SP_DES', "compressed_SP_DES", $work_demos[$i]);
                    // replace ../
                    $work_demos[$i] = str_replace('../', "", $work_demos[$i]);
                    
                    $demo_imgs[$demo_imgs_count] = $work_demos[$i];
                    $demo_imgs_count++;
                    

                }elseif (in_array($ext, $videoExtensions)) {
                    // check if video exists
                    if (file_exists($work_demos[$i]) || file_exists("../".$work_demos[$i])) {
                        $demo_vids[$demo_vid_count] = $work_demos[$i];
                        $demo_vid_count++;
                    }
                }elseif (in_array($ext, $archiveExtensions) || in_array($ext, $documentExtensions) || in_array($ext, $dataExtensions)) {
                    if ($dwn !== "false") {
                        // check if file exists
                        if (file_exists($work_demos[$i]) || file_exists("../".$work_demos[$i])) {
                            $attached_files[$files_count] = $work_demos[$i];
                            $files_count++;
                        }
                    }
                }
            }
        }

        $likes = getSdWorkLikes(base64_encode(maskData($row['sd_work_id'])));
        $views = getSdWorkViews($row['sd_unique_work_id']);
        $post_date = relative_date(unMaskData(base64_decode($row['sd_work_date'])))." ago";

        $row_profile = get_profile_details($row['sd_work_owner']);
        if (!empty($row_profile)) {
            $name = unMaskData(base64_decode($row_profile['first_name']))." ".unMaskData(base64_decode($row_profile['second_name']));
            $prof_pic   = unMaskData(base64_decode($row_profile['prof_pic']));
            if (empty($prof_pic)) {
                $prof_pic = "img/default/user.png";
            }else{
                $prof_pic   = str_replace('SP_DES', "compressed_SP_DES", unMaskData(base64_decode($row_profile['prof_pic'])));
                // replace ../
                $prof_pic = str_replace('../', "", $prof_pic);
                // check if image exists
                if (!file_exists($prof_pic) && !file_exists("../".$prof_pic)) {
                    $prof_pic = $thumb;
                }  
            }
        }else{
            $name = "Unknown";
            $prof_pic = "img/default/user.png";
        }

        $ttl = unMaskData(base64_decode($row['sd_work_tittle']));
        $desc = strip_tags(unMaskData(base64_decode($row['sd_work_desc'])));
        $uniq_work_id = unMaskData(base64_decode($row['sd_unique_work_id']));
        $prof_link = unMaskData(base64_decode($row_profile['profile_link']));
        $ext_link = unMaskData(base64_decode($row['sd_work_link']));
        $type = unMaskData(base64_decode($row['sd_work_type']));
    }

    // Populate the response array
    $response = [
        'post' => [
            'id' => $uniq_work_id,
            'title' => (string)$ttl,
            'description' => $desc,
            'date' => $post_date,
            'external_link' => $ext_link,
            'type' => $type,
            'likes' => $likes,
            'views' => $views,
            'comments' => $total_comments,
            'thumb' => $thumb,
            'category' => [
                'category_name' => $cat_name,
                'category_id' => $cat_id
            ],
            'media' => [
                'images' => $demo_imgs,
                'videos' => $demo_vids
            ],
            'files' => $attached_files,
            'creator' => [
                'name' => $name,
                'profile_picture' => $prof_pic,
                'profile_link' => $prof_link
            ],
            'liked' => $liked,
            'owner' => $owner
        ]
    ];

    return $response;

}

function return_timeline_sd_work($sd_work_id, $add_ad = true, $show_header = true, $show_footer = true) {
    global $con;
    $post = get_sd_work_details($sd_work_id);

    // Initialize necessary variables
    $uniq_work_id = $post['post']['id'];
    $ttl = truncateText($post['post']['title'], 100);
    $desc = truncateText($post['post']['description'], 200);
    $post_date = $post['post']['date'];
    $thumbnailImage = $post['post']['thumb'];
    $type = $post['post']['type'];
    $views = $post['post']['views'];
    $likes = $post['post']['likes'];
    $comments = $post['post']['comments'];
    $name = $post['post']['creator']['name'];
    $prof_pic = $post['post']['creator']['profile_picture'];
    $prof_link = $post['post']['creator']['profile_link'];
    $liked = $post['post']['liked'];
    $owner = $post['post']['owner'];

    $images = $post['post']['media']['images'];
    $videos = $post['post']['media']['videos'];

    $like_class = $liked ? 'liked' : '';

    if ($thumbnailImage){
        $thumb = "<img src='$thumbnailImage' alt='image'>";
    }else{
        $thumb = "";
    }
    

    if ($owner) {

        $menu = "<li><i class='fas fa-solid fa-trash'></i> <a href='?delete=$uniq_work_id'>Delete</a></li>
                <li><i class='fas fa-edit'></i> <a href='?edit=$uniq_work_id'>Edit</a></li>
                ";

        $story_menu = "<li><i class='fas fa-solid fa-trash'></i> <a href='?delete=$uniq_work_id'>Delete</a></li>";
    }else{
        $menu = "<li><i class='fas fa-solid fa-flag'></i> <a href='?report=$uniq_work_id'>Report</a></li>";

        $story_menu = "<li><i class='fas fa-solid fa-flag'></i> <a href='?report=$uniq_work_id'>Report</a></li>";
    }

    $demo_imgs_count = 0;
    $demo_vid_count = 0;
    $extra_demo_imgs = 0;
    $demo_imgs_cont = "";

    for ($i=0; $i < count($images); $i++) {
        if ($demo_imgs_count < 4 && $images[$i] != $thumbnailImage) {
            $demo_imgs_count++;
            if (empty($images[$i])) {
                continue;
            }
            // check if image exists
            if (file_exists($images[$i]) || file_exists("../".$images[$i])) {
                $demo_imgs_cont = $demo_imgs_cont."<div class='spinn_design_work_demo_images'><img src='".$images[$i]."' alt='image'></div>";
            }
        }else{
            if ($images[$i] != $thumbnailImage) {
                $extra_demo_imgs++;
            }
        }
    }

    $demo_vid_count = count($videos);
    if ($demo_vid_count > 0){
        $demo_vid_count = "<span class='spinn_design_work_demo_images extra_demo' data-more='+$demo_vid_count'><i class='fas fa-video'></i></span>";
    }else{
        $demo_vid_count = "";
    }
    if ($extra_demo_imgs > 0){
        $extra_demo_imgs = "<span class='spinn_design_work_demo_images extra_demo' data-more='+$extra_demo_imgs'><i class='fas fa-images'></i></span>";
    }else{
        $extra_demo_imgs = "";
    }

    if (empty($demo_imgs_cont) && empty($demo_vid_count) && empty($extra_demo_imgs)){
        $shared_files = "";
    }else{
        $shared_files = "<div class='spinn_design_work_shared_files'>
                    $demo_imgs_cont
                    $demo_vid_count
                    $extra_demo_imgs
                    </div>";
    }

    if($thumb){
        $thumb = "<div class='spinn_design_work_main_content prev_job' data-id='$uniq_work_id' style='--before-bg-image: url(../$thumbnailImage)'>
                    $thumb
                    $shared_files
                </div>";
    }

    if ($type == "stories") {
        $query_str = "SELECT * FROM `sd_stories` WHERE `sd_story_unique_id` = '".$uniq_work_id."'";
        $result_str = mysqli_query($con, $query_str);

        if ($row_str = mysqli_fetch_assoc($result_str)) {
            $story = createTimelineStoryContainer($row_str);
        } else {
            $story = "";
        }

        if (empty($story)) {
            return $container = "";
        } else {
            $views = totalStoryViews($row_str['sd_story_unique_id']);
        }

        $str_unq_id = unMaskData(base64_decode($row_str['sd_story_unique_id']));
        
        $container =  "<div class='spinn_design_work' data-id='".$uniq_work_id."' data-group='spinn_design_work' data-thumb='../$thumbnailImage'>
            <div class='spinn_design_work_header'>
                <a href='?profile=".$prof_link."'>
                    <span class='profile_pic'>
                        <img src='".$prof_pic."' alt='profile picture'>
                    </span>
                    <span class='profile_name'>".$name."</span>
                </a>
                <span class='upload_time'>".$post_date."</span>
                <button class='spinn_design_work_more_menu'>
                    <i class='fas fa-ellipsis-v'></i>
                    <ul>
                        $story_menu
                    </ul>
                </button>
            </div>
            <div class='spinn_design_work_thumb_desc'>
                <a href='?view_story=$str_unq_id'>$story</a>
            </div>
            <div class='spinn_design_work_footer'>
                <div class='spinn_design_work_info'>
                    <button class='views_count' data-id='$uniq_work_id' title='Views'>
                        <i class='fas fa-eye'></i> $views
                    </button>
                    <button class='like_job $like_class boing' data-id='$uniq_work_id' title='Like'>
                        <span class='likes_count' data-id='$uniq_work_id' title='Likes'>$likes </span>
                        <i class='fas fa-thumbs-up'></i> 
                    </button>
                    <button>
                        <span class='comment_job boing' data-id='$uniq_work_id' title='Comment'>
                        $comments <i class='fas fa-comments'></i> 
                        </span>
                    </button>
                    <button class='share_work cb' data-share-work-id='$uniq_work_id' title='Share'>
                        <i class='fas fa-share-alt-square'></i> 
                    </button>
                </div>
            </div>
        </div>";
    } else {
        $container =  "<div class='spinn_design_work' data-id='$uniq_work_id' data-group='spinn_design_work' data-thumb='../$thumbnailImage' style='--before-bg-image:url(../$thumbnailImage'>
            <div class='spinn_design_work_header'>
                <a href='?profile=$prof_link'>
                    <span class='profile_pic left'>
                        <img src='$prof_pic' alt='profile picture'>
                    </span>
                    <span class='profile_name'>$name</span>
                </a>
                <span class='upload_time'>$post_date</span>
                <button class='spinn_design_work_more_menu'>
                    <i class='fas fa-ellipsis-v'></i>
                    <ul>
                        $menu
                    </ul>
                </button>
            </div>
            <div class='spinn_design_work_thumb_desc'>
                $thumb
                <div class='spinn_design_work_desc_cont'>
                    <div class='spinn_design_work_ttl'><a href='designs/$uniq_work_id' class='prev_job' data-id='$uniq_work_id'>$ttl</a></div>
                    <div class='spinn_design_work_desc'>$desc</div>
                </div>
            </div>
            <div class='spinn_design_work_footer'>
                <div class='spinn_design_work_info'>
                    <button class='views_count' data-id='$uniq_work_id' title='Views'>
                        <i class='fas fa-eye'></i> $views Views
                    </button>
                    <button class='like_job $like_class boing' data-id='$uniq_work_id' title='Like'>
                        <span class='likes_count' data-id='$uniq_work_id' title='Likes'>$likes </span>
                        <i class='fas fa-thumbs-up'></i> Like
                    </button>
                    <button>
                        <span class='comment_job boing prev_job' data-id='$uniq_work_id' title='Comment'>
                        $comments <i class='fas fa-comments'></i> Comment
                        </span>
                    </button>
                    <button class='share_work cb' data-share-work-id='$uniq_work_id' title='Share'>
                        <i class='fas fa-share-alt-square'></i> Share
                    </button>
                </div>
            </div>
        </div>";
    }


    $showAd = array("false", "true", "false", "true", "false", "true", "false");
    $shouldShowAd = array_rand($showAd, 1);
    $adTheme = "theme_".rand(0, 42);

    $ad = "<div class='spinn_design_work timeline_ad' data-group='spinn_design_work'>
                <div class='spinn_design_work_header'>
                    <div class='profile_name more'>Ad</div>
                </div>
                <div class='spinn_design_work_thumb_desc timeline_ad_cont $adTheme'>
                    <ins class='adsbygoogle'
                         style='display:block'
                         data-ad-format='fluid'
                         data-ad-layout-key='-6t+ed+2i-1n-4w'
                         data-ad-client='ca-pub-2317654314735642'
                         data-ad-slot='5861562814'></ins>
                    <script>
                         (adsbygoogle = window.adsbygoogle || []).push({});
                    </script>
                </div>
                <div class='spinn_design_work_footer'>
                </div>
            </div>";

    if ($showAd[$shouldShowAd] == "true" && $add_ad) {
        $container .= $ad;
    }

    return $container;
}

// Unique  key gen
function viewSdWorkKey($c)
{
    global $con;

    $en_c = base64_encode(maskData($c));

    $query = "SELECT * FROM `sd_works` WHERE `sd_unique_work_id` = '".$en_c."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
        generateUniqueSdWorkKey();
    }else{
        return $c;
    }
}

// 
function generateUniqueSdWorkKey()
{
    $c = random_str(8);
    viewSdWorkKey($c);
}

//
function viewSdStoryKey($c)
{
    global $con;

    $en_c = base64_encode(maskData($c));

    $query = "SELECT * FROM `sd_stories` WHERE `sd_story_unique_id` = '".$en_c."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
        generateUniqueSdStoryKey();
    }else{
        return $c;
    }
}

function generateUniqueSdStoryKey()
{
    $c = random_str(8);
    viewSdStoryKey($c);
}

//

//
function viewSdPollKey($c)
{
    global $con;

    $en_c = base64_encode(maskData($c));

    $query = "SELECT * FROM `sd_polls` WHERE `sd_poll_unique_id` = '".$en_c."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
        generateUniqueSdPollKey();
    }else{
        return $c;
    }
}

// 
function generateUniqueSdPollKey()
{
    $c = random_str(10);
    viewSdPollKey($c);
}

//Unique ad Key
function viewSdAdKey($c)
{
    global $con;

    $en_c = base64_encode(maskData($c));

    $query = "SELECT * FROM `sd_ads` WHERE `sd_ad_unq_id` = '".$en_c."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result) || empty($c)) {
        generateUniqueSdAdKey();

    }else{
        return $c;
    }
}

// 
function generateUniqueSdAdKey()
{
    $c = random_str(12);
    viewSdAdKey($c);
}

//
function viewSdNotifKey($c)
{
    global $con;

    $en_c = base64_encode(maskData($c));

    $query = "SELECT * FROM `sd_notifications` WHERE `notification_unique_id` = '".$en_c."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result) || empty($c)) {
        generateUniqueSdNotifKey();

    }else{
        return $c;
    }
}

function generateUniqueSdNotifKey()
{
    $c = random_str(8);
    viewSdNotifKey($c);
}

//
function viewSdAccRecTokenKey($c)
{
    global $con;

    $en_c = base64_encode(maskData($c));

    $query = "SELECT * FROM `sd_account_recovery` WHERE `token` = '".$en_c."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result) || empty($c)) {
        generateUniqueSdAccRecTokenKey();

    }else{
        return $c;
    }
}

function generateUniqueSdAccRecTokenKey()
{
    $c = random_str(4);
    viewSdAccRecTokenKey($c);
}

function isTokenExpired($expirationTime) {
    // Convert expiration time to DateTime object
    $expirationDateTime = new DateTime($expirationTime);

    // Get the current date and time
    $currentDateTime = new DateTime();

    // Compare the current date and time with the expiration time
    return $currentDateTime > $expirationDateTime;
}

function create_notification($notif_tittle, $notif_msg, $notif_to, $notif_link)
{
    global $my_email, $dbh, $tm;

    $c = random_str(8);

    $sql = "INSERT INTO `sd_notifications`(`notification_id`, `notification_unique_id`, `notification_tittle`, `notification_msg`, `notification_to`, `notification_date`, `notification_status`, `notification_link`) VALUES (NULL, :notification_unique_id, :notification_tittle, :notification_msg, :notification_to, :notification_date, :notification_status, :notification_link)";

    $query = $dbh->prepare($sql);

    $unique_id = base64_encode(maskData(viewSdNotifKey($c)));
    $notif_tittle = base64_encode(maskData($notif_tittle));
    $notif_msg = base64_encode(maskData(strip_tags($notif_msg)));
    $notif_to = base64_encode(maskData($notif_to));
    $notif_link = base64_encode(maskData($notif_link));
    $status = base64_encode(maskData("pending"));
    $date = base64_encode(maskData($tm));

    $query->bindParam('notification_unique_id', $unique_id, PDO::PARAM_STR );
    $query->bindParam('notification_tittle', $notif_tittle, PDO::PARAM_STR );
    $query->bindParam('notification_msg', $notif_msg, PDO::PARAM_STR );
    $query->bindParam('notification_to', $notif_to, PDO::PARAM_STR );
    $query->bindParam('notification_date', $date, PDO::PARAM_STR );
    $query->bindParam('notification_status', $status, PDO::PARAM_STR );
    $query->bindParam('notification_link', $notif_link, PDO::PARAM_STR );

    $query->execute();

    return;

}

function mark_notif_read($id)
{
    global $con, $my_email;

    $id = base64_encode(maskData($id));
    $status = base64_encode(maskData("read"));

    $query = "UPDATE `sd_notifications` SET `notification_status` = '".$status."' WHERE `notification_to` = '".$my_email."' AND `notification_unique_id` = '".$id."'";

    $result = mysqli_query($con, $query);
}

if (isset($_GET['sd_notification'])) {
    mark_notif_read($_GET['sd_notification']);
}

function notify_all_members($tittle, $msg, $link)
{

    global $my_email, $con, $tm;

    $query = "SELECT * FROM `user_log_inf` WHERE `email_address` != '".$my_email."'";
    $result = mysqli_query($con, $query);

    while ($row = mysqli_fetch_assoc($result)) {

        create_notification($tittle, $msg, unMaskData(base64_decode($row['email_address'])), $link);

    }
}
//notify_all_members("Welcome", "Welcome to Spinn Code", "#test", $con, $c, $tm, $my_email);
//create_notification("test", "ttx", $my_email, "#sd_work", $con, $c, $tm);

//

// Get post status
function getPostStatus($post_id)
{
    global $con, $tm;

    $post_id_1 = base64_encode(maskData($post_id));

    $query1 = "SELECT * FROM `sd_work_status` WHERE `sd_work_id` = '".$post_id."' OR `sd_work_id` = '".$post_id_1."'";

    $result1 = mysqli_query($con, $query1);

    if ($row1 = mysqli_fetch_assoc($result1)) {
        // Delete after 5 days of deletion by user
        $sts = unMaskData(base64_decode($row1['sd_work_status_label']));
        if ($sts === "delete") {
            // echo $sts;
            if (empty($row1['sd_work_report_date'])) {
                deletePost($row1['sd_work_id']);
            }else{
                $current_date = ($tm);
                $report_date = unMaskData(base64_decode($row1['sd_work_report_date']));

                $relative_short_date = round(((((strtotime($current_date) - strtotime($report_date))/60)*100)/100));

                if ($relative_short_date >= 5) {
                    deletePost($row1['sd_work_id']);
                }
            }
        }
        return 0;
    }else{
        return 1;
    }
}

function getPostDetails($post_id)
{
    global $con;

    $enc_post_id = base64_encode(maskData($post_id));

    $sql = "SELECT * FROM `sd_works` WHERE `sd_unique_work_id` = '".$enc_post_id."' OR `sd_work_id` = '".$post_id."'";

    $query = mysqli_query($con, $sql);

    if ( $result = mysqli_fetch_array($query) ) {
        return $result;
    }else{
        return $result = "";
    }
}

function get_my_custom_pages($email)
{
    global $con;

    $sql = "SELECT * FROM `sd_works` WHERE `sd_work_owner` = '".$email."'";

    $query = mysqli_query($con, $sql);

    $page_link = "";
    $index = 0;
    while ( $result = mysqli_fetch_array($query) ) {

        $cat = base64_encode(maskData($result['sd_work_cat']));

        if (get_cat_name($result['sd_work_cat']) == "page") {
            $index++;
            $link = base64_encode(maskData($result['sd_unique_work_id']));
            $desc = base64_encode(maskData($result['sd_work_desc']));
            $ttl = base64_encode(maskData($result['sd_work_tittle']));

            $page_link .= "($index) <a href='pages/$link' tittle='$desc'>$ttl</a>  <br>";
        }
    }
    return $page_link;
}

// DetectBase64Encode
function is_base64_encoded($data)
{
    $decoded = base64_decode($data);

    if ( base64_encode($decoded) === $data){
        return true;
    } else {
        return false;
    }
};

// Get total likes
function getSdWorkLikes($work_id)
{
    global $con;

    $enc = base64_encode(maskData("liked"));

    $query = "SELECT * FROM `sd_works_ratings` WHERE `sd_work_id` = '".$work_id."' AND `sd_rate_work_status` = '".$enc."'";

    $result = mysqli_query($con, $query);

    $likes = mysqli_num_rows($result);


    return $likes;

}

// Get total views
function getSdWorkViews($work_id)
{
    global $con;

    $query = "SELECT * FROM `sd_work_views` WHERE `sd_work_view_unq_id` = '".$work_id."'";

    $result = mysqli_query($con, $query);

    $views = mysqli_num_rows($result);


    return $views;

}

// Get my like
function getMyLike($work_id)
{
    global $con, $my_email;

    // DEPRECIATED
    // if (empty($my_email)) {
	// 	$my_email = base64_encode(maskData(getUserIpAddr()));
	// }

    if (empty($my_email)) {
        // Use cookie ID
        // Check if the cookie is set
        if (!isset($_COOKIE['user_id'])) {
            return false; // Cookie is not set; the user cannot like
        }

        $user_id = $_COOKIE['user_id']; // Retrieve the unique user identifier from the cookie

        $my_email = $user_id;
    }

    $sts = base64_encode(maskData("liked"));

    $query = "SELECT * FROM `sd_works_ratings` WHERE `sd_work_id` = '".$work_id."' AND `sd_rate_work_status` = '".$sts."' AND `sd_work_rate_email` = '".$my_email."'";

    $result = mysqli_query($con, $query);

    if (mysqli_fetch_assoc($result)) {
        return true; // User has liked this work
    } else {
        return false; // User has not liked this work
    }
}

$encription_key = "mbyXk2AseFMMDeqcyy5vGoAkMYLYpcmc";
$iv = "ofhltTTmtu6BaV83";
//$iv = random_str(16);

// Encription
function maskData($data)
{
    global $encription_key, $iv;

    $enc_data = @openssl_encrypt(pkcs7_pad($data, 16),
        'AES-256-CBC',
        $encription_key,
        0,
        $iv
    );

    return $enc_data;
}

// 
function pkcs7_pad($data, $size)
{
    $length = $size - strlen($data) % $size;
    return $data . str_repeat(chr($length), $length);
}

// Decrypt
function unMaskData($data)
{
    global $encription_key, $iv;

    $dec_data = pkcs7_uvnpad(openssl_decrypt(
        $data,
        'AES-256-CBC',
        $encription_key,
        0,
        $iv
    ));

    return $dec_data;
}

// 
function pkcs7_uvnpad($data)
{
    if (is_bool($data)) {
        return $data;
    }
    return substr($data, 0, -ord($data[strlen($data) - 1]));
}

// Hash Pass
function hashPass($pass)
{
    $random = "89tsp3lxuuoWRQjmAOaraWe1PqGV8Al";
    //$random = openssl_random_pseudo_bytes(18);

    $salt = sprintf(
        '$2y$%02d$%s',
        13,
        substr(strtr(base64_encode($random), '+', '.'), 0, 22)
    );

    $hash = crypt($pass, $salt);
}

// ReHash Pass
function unhashPass($given_pass, $db_hash)
{
    $given_hash = crypt($given_pass, $db_hash);

    if (isEqual($given_pass, $db_hash)) {
        return true;
    }else{
        return false;
    }
}

// Str compare
function isEqual($str1, $str2)
{
    $n1 = strlen($str1);
    $n2 = strlen($str2);

    if ($n1 != $n2) {
        return false;
    }

    for ($i=0, $diff = 0; $i != $n1; $i++) {
        $diff |= ord($str1[$i]) ^ ord($str2[$i]);
    }
    return !$diff;
}

// Get post images
function get_post_images($sd_work_id)
{
    global $con, $imageExtensions;
    $query = "SELECT * FROM `sd_works` WHERE `sd_work_id` = '".$sd_work_id."'";

    $result = mysqli_query($con, $query);

    $post_images = array();

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

        $demo_imgs = unMaskData(base64_decode($row['sd_work_demos']));
        $demo_imgs = explode('XSPDX', $demo_imgs);

        for ($i=0; $i < count($demo_imgs); $i++) {
            if (!empty($demo_imgs[$i])) {

                $ext = explode('.', $demo_imgs[$i]);
                $ext = strtolower(end($ext));

                if (in_array($ext, $imageExtensions)) {

                    $demo_imgs[$i]= str_replace('SP_DES', "compressed_SP_DES", $demo_imgs[$i]);
                    // check if image exists
                    if (!file_exists($demo_imgs[$i]) && !file_exists("../".$demo_imgs[$i])) {
                        $demo_imgs[$i] = "img/default/no_image.png";
                    }else{
                    }

                    array_push($post_images, $demo_imgs[$i]);

                }
            }
        }

    }

    return $post_images;

}

// Get post videos
function get_post_videos($sd_work_id)
{
    global $con, $videoExtensions;
    $query = "SELECT * FROM `sd_works` WHERE `sd_work_id` = '".$sd_work_id."'";

    $result = mysqli_query($con, $query);

    $post_vids = array();

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

        $demo_vids = unMaskData(base64_decode($row['sd_work_demos']));
        $demo_vids = explode('XSPDX', $demo_vids);

        for ($i=0; $i < count($demo_vids); $i++) {
            if (!empty($demo_vids[$i])) {

                $ext = explode('.', $demo_vids[$i]);
                $ext = strtolower(end($ext));

                if (in_array($ext, $videoExtensions)) {

                    array_push($post_vids, $demo_vids[$i]);

                }
            }
        }

    }

    return $post_vids;
}


// if i viewed story
function iViewedStory($uniqueId)
{
    global $my_email, $con;

    $query = "SELECT * FROM `sd_stories_view` WHERE `sd_story_viewer` = '".$my_email."' AND `sd_story_uniq_id` = '".$uniqueId."'";
    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
        return true;
    }else{
        return false;
    }
}

// total srory views
function totalStoryViews($uniqueId)
{
    global $con;

    $query = "SELECT * FROM `sd_stories_view` WHERE `sd_story_uniq_id` = '".$uniqueId."'";
    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
        return mysqli_num_rows($result);
    }else{
        return 0;
    }
}

// Status expired
function statusExpired($uniqueId)
{
    global $con, $tm;
    $query = "SELECT * FROM `sd_stories` WHERE `sd_story_unique_id` = '".$uniqueId."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
        $status_duration = unMaskData(base64_decode($row['sd_story_duration']));
        $status_date = unMaskData(base64_decode($row['sd_story_date']));
        $sts_media = unMaskData(base64_decode($row['sd_story_media']));

        if (empty($status_date) || empty($status_duration)) {
            return true;
        }else{

            $current_date = ($tm);

            $relative_short_date = round(((((strtotime($current_date) - strtotime($status_date))/60)*100)/100));

            $relative_short_date = round(($relative_short_date/60));

            if (($relative_short_date - $status_duration) > 0) {

                deleteStory($uniqueId);

                return true;
            }else{
                return false;
            }
        }
    }else{
        return true;
    }

}

// Poll expired
function pollExpired($enc_uniqueId)
{
    global $con, $tm;
    $query = "SELECT * FROM `sd_polls` WHERE `sd_poll_unique_id` = '".$enc_uniqueId."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
        $poll_duration = unMaskData(base64_decode($row['sd_poll_duration']));
        $poll_date = unMaskData(base64_decode($row['sd_poll_date']));

        if (empty($poll_date) || empty($poll_date)) {
            return true;
        }else{

            $current_date = ($tm);

            $relative_short_date = round(((((strtotime($current_date) - strtotime($poll_date))/60)*100)/100));

            $relative_short_date = round(($relative_short_date/60));

            if (($relative_short_date - $poll_duration) > 0) {

                //deletePoll($uniqueId);

                return true;
            }else{
                return false;
            }
        }
    }else{
        return true;
    }

}

// Delete story
function deleteStory($uniqueId)
{
    global $con, $my_email;

    $query = "SELECT * FROM `sd_stories` WHERE `sd_story_unique_id` = '".$uniqueId."' AND `sd_story_owner` = '".$my_email."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

        if (!empty($sts_media)) {
            if (file_exists("../".$sts_media)){
                unlink("../".$sts_media);
            }

            $sts_media = str_replace('SP_DES', "compressed_SP_DES", $sts_media);

            if (file_exists("../".$sts_media)){
                unlink("../".$sts_media);
            }
        }

        $query = "DELETE FROM  `sd_stories` WHERE `sd_story_unique_id` = '".$uniqueId."'";

        $result = mysqli_query($con, $query);

        $query = "DELETE FROM  `sd_stories_view` WHERE `sd_story_uniq_id` = '".$uniqueId."'";

        $result = mysqli_query($con, $query);

        return true;
    }else{
        return false;
    }
}

// Get new stories
function getNewStories()
{
    global $con, $my_email;

    $query = "SELECT * FROM `sd_stories` WHERE `sd_story_owner` != '".$my_email."' ORDER BY `sd_story_unique_id` DESC";

    $result = mysqli_query($con, $query);

    $new_story = [];

    while ($row = mysqli_fetch_assoc($result)) {
        if (!iViewedStory($row['sd_story_unique_id'])) {
            $new_story[] = $row;
        }
    }

    return $new_story;

}

// Get viewed stories
function getViewedStories()
{
    global $con, $my_email;

    $query = "SELECT * FROM `sd_stories` WHERE `sd_story_owner` != '".$my_email."' ORDER BY `sd_story_unique_id` DESC";

    $result = mysqli_query($con, $query);

    $viewed_story = [];

    while ($row = mysqli_fetch_assoc($result)) {
        if (iViewedStory($row['sd_story_unique_id'])) {
            $viewed_story[] = $row;
        }
    }

    return $viewed_story;
}

// Get my stories
function getMyStories()
{
    global $con, $my_email;

    $query = "SELECT * FROM `sd_stories` WHERE `sd_story_owner` = '".$my_email."' ORDER BY `sd_story_unique_id` DESC";

    $result = mysqli_query($con, $query);

    $my_stories = [];

    while ($row = mysqli_fetch_assoc($result)) {
        if (!statusExpired($row['sd_story_unique_id'])) {
            $my_stories[] = $row;
        }
    }

    return $my_stories;

}

// Ministory cont
function createMiniStoryContainer($row)
{
    global $imageExtensions, $videoExtensions;

    $theme = unMaskData(base64_decode($row['sd_story_theme']));
    $ppic = get_profile_details($row['sd_story_owner'])['prof_pic'];
    $ppic = unMaskData(base64_decode($ppic));
    $quote = unMaskData(base64_decode($row['sd_story_parent']));
    $media = unMaskData(base64_decode($row['sd_story_media']));
    $unq_id = unMaskData(base64_decode($row['sd_story_unique_id']));

    if (!statusExpired($row['sd_story_unique_id'])) {

        if (!empty($media) || $media !== "none") {
            $ext = explode('.', $media);
            $ext = strtolower(end($ext));

            if (in_array($ext, $imageExtensions)) {
                $media = str_replace('SP_DES', "compressed_SP_DES", $media);
                // check if media is exist
                if (file_exists("../".$media)) {
                    $media = "img/default/no_image.png";
                }
                $media = "<img src='$media' alt='image'>";
            }elseif (in_array($ext, $videoExtensions)) {
                $media = "<video src='$media'></video>";
            }else{
                $media = "";
            }
        }

        if (empty($ppic)) {
            $ppic = "assets/images/logo.svg";
        }

        if (iViewedStory($row['sd_story_unique_id']) == true) {
            $viewed_class = "sd_viewed_mini_sts";
        }else{
            $viewed_class = "sd_new_mini_sts";
        }

        $container = "<div class='sd_status_cont_min $viewed_class'>
                <a href='?view_story=$unq_id'>
                    <div class='sd_status_bg $theme'></div>
                    <div class='sd_status_media'>
                        <div class='sd_status_media_container'>$media</div>
                    </div>
                    <div class='sd_status_min_quote'>$quote</div>
                    <div class='sd_status_cont_min_prof_pic'>
                        <img src='$ppic' alt='profile picture'>
                    </div>
                </a>
            </div>";
    }else{
        $container = "";
    }

    return $container;
}

// Maxstory cont
function createMaxStoryContainer($row)
{
    global $imageExtensions, $videoExtensions, $my_email;

    if (!statusExpired($row['sd_story_unique_id'])) {

        if (iViewedStory($row['sd_story_unique_id']) == true) {
            $viewed_sts = "true";
        }else{
            $viewed_sts = "false";
        }

        $id = $row['sd_story_id'];
        $theme = unMaskData(base64_decode($row['sd_story_theme']));
        $profile = get_profile_details($row['sd_story_owner']);
        $ppic = unMaskData(base64_decode($profile['prof_pic']));
        $fname = unMaskData(base64_decode($profile['first_name']));
        $sname = unMaskData(base64_decode($profile['second_name']));
        $quote = unMaskData(base64_decode($row['sd_story_parent']));
        $media = unMaskData(base64_decode($row['sd_story_media']));
        $unq_id = unMaskData(base64_decode($row['sd_story_unique_id']));
        $sts_tm = unMaskData(base64_decode($row['sd_story_date']));
        $type = unMaskData(base64_decode($row['sd_story_type']));
        $link = $row['sd_story_link'];

        $sts_tm = relative_date($sts_tm);

        if (empty($ppic)) {
            $ppic = "assets/images/logo.svg";
        }

        if (!empty($media) || $media !== "none") {
            $ext = explode('.', $media);
            $ext = strtolower(end($ext));

            if (in_array($ext, $imageExtensions)) {
                $media = "<img data-src='$media' class='swiper-lazy sd_status_media_cont' data-type='image' id='sts_media_$unq_id'>";
                $media_type = "image";
            }elseif (in_array($ext, $videoExtensions)) {
                $media = "<video data-src='$media' class='swiper-lazy sd_status_media_cont' data-type='video' id='sts_media_$unq_id'></video>";
                $media_type = "video";
            }else{
                $media = "";
                $media_type = "";
            }
        }

        if ($row['sd_story_owner'] === "$my_email") {
            $story_views = "<span>".totalStoryViews($row['sd_story_unique_id'])."<i class='fas fa-eye'></i></span>
                <button class='spinn_design_work_more_menu'>
                    <i class='fas fa-ellipsis-v'></i>
                    <ul>
                        <li onclick='delete_story(`$unq_id`)'><i class='fa-solid fa-trash'></i> Delete</li>
                    </ul>
                </button>
            ";
        }else{
            $story_views = "";

        }


        if ($type === "poll") {
            $poll_cont = "<div class='sd_story_poll'>".return_timeline_poll_cont($link)."</div>";
        }else{
            $poll_cont = "";
        }

        $container = "<div class='swiper-slide sd_status_cont' data-id='$unq_id' data-viewed='$viewed_sts' data-type='$media_type'>
                <div class='sd_status_profile'>
                    <div class='sd_status_profile_pic'>
                        <img data-src='$ppic' class='swiper-lazy'>
                    </div>
                    <div class='sd_status_profile_name'>
                        <div>$fname $sname</div> 
                        <div>$sts_tm ago</div>
                    </div>
                </div>
                <div class='sd_status_bg $theme'></div>
                <div class='sd_status_media'>
                    <div class='sd_status_media_container'>$media</div>
                    <div class='transluscent_overlay' id='sd_status_media_overlay_$unq_id'><div class='lds-roller'><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div></div>
                </div>
                <div class='preview_quote'>
                    $quote
                    $poll_cont
                </div>

                <div class='sd_status_footer'>
                    $story_views
                </div>
            </div>";

    }else{
        $container = "";
    }

    return $container;
}

// Timelinestory cont
function createTimelineStoryContainer($row)
{
    global $imageExtensions, $videoExtensions, $my_email;

    if (!statusExpired($row['sd_story_unique_id'])) {

        if (iViewedStory($row['sd_story_unique_id']) == true) {
            $viewed_sts = "true";
        }else{
            $viewed_sts = "false";
        }

        $id = $row['sd_story_id'];
        $theme = unMaskData(base64_decode($row['sd_story_theme']));
        $profile = get_profile_details($row['sd_story_owner']);
        $ppic = unMaskData(base64_decode($profile['prof_pic']));
        $fname = unMaskData(base64_decode($profile['first_name']));
        $sname = unMaskData(base64_decode($profile['second_name']));
        $quote = unMaskData(base64_decode($row['sd_story_parent']));
        $media = unMaskData(base64_decode($row['sd_story_media']));
        $unq_id = unMaskData(base64_decode($row['sd_story_unique_id']));
        $sts_tm = unMaskData(base64_decode($row['sd_story_date']));

        $sts_tm = relative_date($sts_tm);

        if (!empty($media) || $media !== "none") {
            $ext = explode('.', $media);
            $ext = strtolower(end($ext));

            if (in_array($ext, $imageExtensions)) {
                $media = "<img src='$media' class='sd_status_media_cont' data-type='image' alt='image'><span class='sd_status_media_icn'><i class='fas fa-images'></i><span>";
                $media_type = "image";
            }elseif (in_array($ext, $videoExtensions)) {
                $media = "<video src='$media' class='sd_status_media_cont timeline_video' data-type='video'></video><span class='sd_status_media_icn'><i class='fas fa-video'></i><span>";
                $media_type = "video";
            }else{
                $media = "";
                $media_type = "";
            }
        }

        $container = "<div class='sd_status_cont'>
                <div class='sd_status_bg $theme'></div>
                <div class='sd_status_media'>
                    <div class='sd_status_media_container'>$media</div>
                </div>
                <div class='preview_quote'>
                     $quote
                </div>
            </div>";

    }else{
        $container = "";
    }

    return $container;
}

// Share story to timeline
function storyToTimeline($uniqueId)
{
    global $con, $my_email, $dbh, $tm;

    if (!statusExpired($uniqueId)) {
        $query = "SELECT * FROM `sd_stories` WHERE `sd_story_owner` = '".$my_email."' AND `sd_story_unique_id` = '".$uniqueId."'";

        $result = mysqli_query($con, $query);

        if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
            $query = "SELECT * FROM `sd_works` WHERE `sd_work_owner` = '".$my_email."' AND `sd_work_link` = '".$uniqueId."'";
            $result = mysqli_query($con, $query);

            if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

                return true;
            }else{

                $sd_work_type = base64_encode(maskData("stories"));

                $sd_work_link = $uniqueId;

                $work_cat = base64_encode(maskData(strtolower("stories")));

                $work_cat_id = get_cat_id($work_cat);

                $c = random_str(8);

                $uniqueId = viewSdWorkKey($c);

                $sql = "INSERT INTO `sd_works`(`sd_work_id`, `sd_work_tittle`, `sd_work_desc`, `sd_work_thumb`, `sd_work_demos`, `sd_work_date`, `sd_work_cat`, `sd_work_post_status`, `sd_work_owner`, `sd_unique_work_id`, `sd_work_search_phrase`, `sd_work_type`, `sd_work_link`)  VALUES (NULL, '', '', '', '', :sd_work_date, :sd_work_cat, :sd_work_post_status, :sd_work_owner, :sd_unique_work_id, '', :sd_work_type, :sd_work_link)";

                $query = $dbh->prepare($sql);

                $sts = base64_encode(maskData("complete"));
                $date = base64_encode(maskData($tm));
                $uniqueId = base64_encode(maskData($uniqueId));
                $enc_work_cat_id = base64_encode(maskData($work_cat_id));

                $query->bindParam('sd_work_date', $date, PDO::PARAM_STR );
                $query->bindParam('sd_work_cat', $enc_work_cat_id, PDO::PARAM_STR );
                $query->bindParam('sd_work_post_status', $sts, PDO::PARAM_STR );
                $query->bindParam('sd_work_owner', $_SESSION['spinn_design_user'], PDO::PARAM_STR );
                $query->bindParam('sd_unique_work_id', $uniqueId, PDO::PARAM_STR );
                $query->bindParam('sd_work_link', $sd_work_link, PDO::PARAM_STR );
                $query->bindParam('sd_work_type', $sd_work_type, PDO::PARAM_STR );

                $query->execute();

                return true;
            }
        }else{
            return false;
        }
    }

}


// Share poll to timeline
function pollToTimeline($enc_uniqueId)
{
    global $con, $my_email, $dbh, $tm;

    if (!pollExpired($enc_uniqueId)) {
        $query = "SELECT * FROM `sd_polls` WHERE `sd_poll_owner` = '".$my_email."' AND `sd_poll_unique_id` = '".$enc_uniqueId."'";

        $result = mysqli_query($con, $query);

        if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
            $query = "SELECT * FROM `sd_works` WHERE `sd_work_owner` = '".$my_email."' AND `sd_work_link` = '".$enc_uniqueId."'";
            $result = mysqli_query($con, $query);

            if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
                return true;
            }else{

                $sd_work_type = base64_encode(maskData("poll"));

                $sd_work_link = $enc_uniqueId;

                $work_cat = base64_encode(maskData(strtolower("poll")));

                $work_cat_id = get_cat_id($work_cat);

                $c = random_str(8);

                $uniqueId = viewSdWorkKey($c);

                $link = $uniqueId;

                $sql = "INSERT INTO `sd_works`(`sd_work_id`, `sd_work_tittle`, `sd_work_desc`, `sd_work_thumb`, `sd_work_demos`, `sd_work_date`, `sd_work_cat`, `sd_work_post_status`, `sd_work_owner`, `sd_unique_work_id`, `sd_work_search_phrase`, `sd_work_type`, `sd_work_link`)  VALUES (NULL, '', '', '', '', :sd_work_date, :sd_work_cat, :sd_work_post_status, :sd_work_owner, :sd_unique_work_id, '', :sd_work_type, :sd_work_link)";

                $query = $dbh->prepare($sql);

                $sts = base64_encode(maskData("complete"));
                $date = base64_encode(maskData($tm));
                $uniqueId = base64_encode(maskData($uniqueId));
                $enc_work_cat_id = base64_encode(maskData($work_cat_id));

                $query->bindParam('sd_work_date', $date, PDO::PARAM_STR );
                $query->bindParam('sd_work_cat', $enc_work_cat_id, PDO::PARAM_STR );
                $query->bindParam('sd_work_post_status', $sts, PDO::PARAM_STR );
                $query->bindParam('sd_work_owner', $_SESSION['spinn_design_user'], PDO::PARAM_STR );
                $query->bindParam('sd_unique_work_id', $uniqueId, PDO::PARAM_STR );
                $query->bindParam('sd_work_link', $sd_work_link, PDO::PARAM_STR );
                $query->bindParam('sd_work_type', $sd_work_type, PDO::PARAM_STR );

                $query->execute();

                // Notification
                $prof = get_profile_details($my_email);
                $prof_name = unMaskData(base64_decode($prof['first_name']));
                notify_all_members("Let's hear your opinion", $prof_name." just uploaded a new poll. Click open to vote", "?sd_work=".$link);

                return true;
            }
        }else{
            return false;
        }
    }

}

// Share poll to story
function pollToStory($enc_uniqueId)
{
    global $con, $my_email, $dbh, $tm;

    if (!pollExpired($enc_uniqueId)) {
        $query = "SELECT * FROM `sd_polls` WHERE `sd_poll_owner` = '".$my_email."' AND `sd_poll_unique_id` = '".$enc_uniqueId."'";

        $result = mysqli_query($con, $query);

        if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

            $story_duration = $row['sd_poll_duration'];
            $story_date = $row['sd_poll_date'];

            $query = "SELECT * FROM `sd_stories` WHERE `sd_story_owner` = '".$my_email."' AND `sd_story_link` = '".$enc_uniqueId."'";
            $result = mysqli_query($con, $query);

            if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
                return true;
            }else{

                $sd_work_type = base64_encode(maskData("poll"));

                $sd_work_link = $enc_uniqueId;

                $work_cat = base64_encode(maskData(strtolower("poll")));

                $work_cat_id = get_cat_id($work_cat);

                $c = random_str(8);

                $uniqueId = viewSdStoryKey($c);
                $link = $uniqueId;

                $sql = "INSERT INTO `sd_stories`(`sd_story_id`, `sd_story_unique_id`, `sd_story_media`, `sd_story_parent`, `sd_story_owner`, `sd_story_duration`, `sd_story_date`, `sd_story_theme`, `sd_story_type`, `sd_story_link`) VALUES (NULL, :sd_story_unique_id, :sd_story_media, :sd_story_parent, :sd_story_owner, :sd_story_duration, :sd_story_date, :sd_story_theme, :sd_story_type, :sd_story_link)";

                $query = $dbh->prepare($sql);

                $uniqueId = base64_encode(maskData($uniqueId));

                // White theme
                $story_theme = base64_encode(maskData("theme_21"));
                $story_parent = "";
                $story_media = "";

                $query->bindParam('sd_story_unique_id', $uniqueId, PDO::PARAM_STR );
                $query->bindParam('sd_story_media', $story_media, PDO::PARAM_STR );
                $query->bindParam('sd_story_parent', $story_parent, PDO::PARAM_STR );
                $query->bindParam('sd_story_owner', $my_email, PDO::PARAM_STR );
                $query->bindParam('sd_story_duration', $story_duration, PDO::PARAM_STR );
                $query->bindParam('sd_story_date', $story_date, PDO::PARAM_STR );
                $query->bindParam('sd_story_theme', $story_theme, PDO::PARAM_STR );
                $query->bindParam('sd_story_type', $sd_work_type, PDO::PARAM_STR );
                $query->bindParam('sd_story_link', $sd_work_link, PDO::PARAM_STR );

                $query->execute();

                // Notification
                $prof = get_profile_details($my_email);
                $prof_name = unMaskData(base64_decode($prof['first_name']));
                notify_all_members("Let's here your opinion", $prof_name." just uploaded a new. Click open to vote", "?view_story=".$link);

                return true;
            }
        }else{
            return false;
        }
    }

}

// Delete poll
function deletePoll($uniqueId)
{
    global $con, $my_email;

    $query = "SELECT * FROM `sd_polls` WHERE `sd_poll_unique_id` = '".$uniqueId."' AND `sd_poll_owner` = '".$my_email."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

        // Check stories
        $query = "SELECT * FROM `sd_stories` WHERE `sd_story_link` = '".$uniqueId."' AND `sd_story_owner` = '".$my_email."'";

        $result = mysqli_query($con, $query);

        if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
            deleteStory($row['sd_story_unique_id']);
        }

        // Check timeline
        $query = "SELECT * FROM `sd_works` WHERE `sd_work_link` = '".$uniqueId."' AND `sd_work_owner` = '".$my_email."'";

        $result = mysqli_query($con, $query);

        if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
            deletePost($row['sd_unique_work_id']);
        }

        $query = "DELETE FROM  `sd_polls` WHERE `sd_poll_unique_id` = '".$uniqueId."'";

        $result = mysqli_query($con, $query);

        $query = "DELETE FROM  `sd_poll_votes` WHERE `sd_poll_vote_unique_id` = '".$uniqueId."'";

        $result = mysqli_query($con, $query);

        return true;
    }else{
        return false;
    }
}

// Delete post
function deletePost($uniqueId)
{
    global $con, $my_email;

    $dec_id = unMaskData(base64_decode($uniqueId));

    $query = "SELECT * FROM `sd_works` WHERE `sd_unique_work_id` = '".$uniqueId."' OR `sd_work_id` = '".$dec_id."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

        if ($row['sd_work_owner'] != $my_email) {
            return false;
        }

        $uniqueId = $row['sd_unique_work_id'];

        $enc_id = base64_encode(maskData($row['sd_work_id']));

        $cat_id = unMaskData(base64_decode($row['sd_work_cat']));
        $cat_name = unMaskData(base64_decode(get_cat_name($cat_id)));

        // Delete other files
        if (!empty($row['sd_work_thumb'])) {
            $thumb = unMaskData(base64_decode($row['sd_work_demos']));
            if (file_exists("../".$thumb)) {
                unlink("../".$thumb);
            }

            $thumb = str_replace('SP_DES', "compressed_SP_DES", $thumb);
            if (file_exists("../".$thumb)) {
                unlink("../".$thumb);
            }
        }

        if (!empty($row['sd_work_demos'])) {
            $demo_imgs = unMaskData(base64_decode($row['sd_work_demos']));
            $demo_imgs = explode('XSPDX', $demo_imgs);

            for ($i=0; $i < count($demo_imgs); $i++) {
                if (!empty($demo_imgs[$i])) {

                    if (file_exists("../".$demo_imgs[$i])) {
                        unlink("../".$demo_imgs[$i]);
                    }

                    $demo_imgs[$i] = str_replace('SP_DES', "compressed_SP_DES", $demo_imgs[$i]);
                    if (file_exists("../".$demo_imgs[$i])) {
                        unlink("../".$demo_imgs[$i]);
                    }

                }
            }
        }

        if ($cat_name === "page") {
            // Delete page files
            $dec_unq_id = unMaskData(base64_decode($row['sd_unique_work_id']));
            if (is_dir("../pages/".$dec_unq_id)) {
                rmdir("../pages/".$dec_unq_id);
            }

            $query = "SELECT * FROM `sd_work_filee_download_status` WHERE `sd_work_id` = '".$uniqueId."' AND `sd_work_owner` = '".$my_email."'";

            $result = mysqli_query($con, $query);

            if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
                if (!empty($row['sd_work_source_file'])) {
                    $source = unMaskData(base64_decode($row['sd_work_source_file']));

                    if (file_exists("../".$source)) {
                        unlink("../".$source);
                    }
                }
            }
        }

        // Delete from status reports
        $query = "DELETE FROM `sd_work_status` WHERE `sd_work_id` = '".$uniqueId."' OR `sd_work_id` = '".$enc_id."'";
        $result = mysqli_query($con, $query);

        // Delete from ratings
        $query = "DELETE FROM `sd_works_ratings` WHERE `sd_work_id` = '".$uniqueId."' OR `sd_work_id` = '".$enc_id."'";
        $result = mysqli_query($con, $query);

        // Delete from database
        $query = "DELETE FROM `sd_works` WHERE `sd_unique_work_id` = '".$uniqueId."' OR `sd_work_id` = '".$enc_id."'";
        $result = mysqli_query($con, $query);

        return true;
    }else{
        return false;
    }
}

// Android apk login
function app_login($username, $app_key)
{
    global $con, $dbh, $tm, $my_email, $_POST;
    $data['new_app_key'] = "";
    $data['new_app_name'] = "";
    $data['response'] = ' no res';
    $data['login_response'] = "Login failed. Please try again.";
    $data['register_response'] = "Registration failed. Please try again.";

    if (!empty($username) && !empty($app_key) || isset($_SESSION['spinn_design_user'])) {

        $query = "SELECT * FROM `sd_user_online_info` WHERE `user_online_info_app_key` = '".$app_key."' AND `user_online_info_name` = '".$username."'";
        $result = mysqli_query($con, $query);

        if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

            $unq_id = $row['user_online_info_unq_id'];

            $sql = "UPDATE `sd_user_online_info` SET `user_online_info_app_key` = :user_online_info_app_key,`user_online_info_name` = :user_online_info_name,`user_online_info_last_update` = :user_online_info_last_update WHERE `user_online_info_unq_id` = :user_online_info_unq_id";

            $data['response'] = 'Update';

        }else{

            if (isset($_SESSION['spinn_design_user']) && isset($_POST['user_login']) && isset($_POST['register_user'])) {

                $query = "SELECT * FROM `user_log_inf` WHERE `email_address`='".$_SESSION['spinn_design_user']."'";

                $result = mysqli_query($con, $query);

                if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

                    $unq_id = $_SESSION['spinn_design_user'];

                    $query = "SELECT * FROM `sd_user_online_info` WHERE `user_online_info_unq_id` = '".$my_email."'";

                    $result = mysqli_query($con, $query);

                    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

                        $sql = "UPDATE `sd_user_online_info` SET `user_online_info_app_key` = :user_online_info_app_key,`user_online_info_name` = :user_online_info_name,`user_online_info_last_update` = :user_online_info_last_update WHERE `user_online_info_unq_id` = :user_online_info_unq_id";

                        $data['response'] = 'Update 2';

                    }else{

                        $sql = "INSERT INTO `sd_user_online_info`(`user_online_info_id`, `user_online_info_unq_id`, `user_online_info_app_key`, `user_online_info_name`, `user_online_info_last_update`) VALUES (NULL, :user_online_info_unq_id, :user_online_info_app_key, :user_online_info_name, :user_online_info_last_update)";
                        $data['response'] = 'Insert';

                    }

                }
            }else {

                $query = "SELECT * FROM `user_log_inf` WHERE `email_address`='".$username."' AND `login_key` = '".$app_key."'";
                $result = mysqli_query($con, $query);

                if ($row = mysqli_fetch_assoc($result)) {

                    $unq_id = $row['email_address'];

                    $query = "SELECT * FROM `sd_user_online_info` WHERE `user_online_info_unq_id` = '".$unq_id."'";
                    $result = mysqli_query($con, $query);
                    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

                        $sql = "UPDATE `sd_user_online_info` SET `user_online_info_app_key` = :user_online_info_app_key,`user_online_info_name` = :user_online_info_name,`user_online_info_last_update` = :user_online_info_last_update WHERE `user_online_info_unq_id` = :user_online_info_unq_id";

                        $data['response'] = 'Update 3';

                    }else{

                        $sql = "INSERT INTO `sd_user_online_info`(`user_online_info_id`, `user_online_info_unq_id`, `user_online_info_app_key`, `user_online_info_name`, `user_online_info_last_update`) VALUES (NULL, :user_online_info_unq_id, :user_online_info_app_key, :user_online_info_name, :user_online_info_last_update)";
                        $data['response'] = 'Insert 2';

                    }

                    $data['reload'] = '1';

                }

            }
        }

        // 
        if (!empty($sql) && !empty($unq_id)) {
            $new_app_key = random_str(24);
            $new_us_name = random_str(24);

            $query = $dbh->prepare($sql);

            $new_app_key = base64_encode(maskData($new_app_key));
            $new_us_name = base64_encode(maskData($new_us_name));
            $date = base64_encode(maskData($tm));

            $query->bindParam('user_online_info_last_update', $date, PDO::PARAM_STR );
            $query->bindParam('user_online_info_unq_id', $unq_id, PDO::PARAM_STR );
            $query->bindParam('user_online_info_app_key', $new_app_key, PDO::PARAM_STR );
            $query->bindParam('user_online_info_name', $new_us_name, PDO::PARAM_STR );

            if (!isset($_POST['key_jst_com'])) {
                $query->execute();
                $data['update_key'] = "true";
            }

            if (!isset($_SESSION['spinn_design_user']) || $_SESSION['spinn_design_user'] !== $unq_id) {
                $_SESSION['spinn_design_user'] = $unq_id;
                $data['reload'] = '1';
                $my_email = $unq_id;
            }

            $data['new_app_key'] = $new_app_key;
            $data['new_app_name'] = $new_us_name;
            $data['login_response'] = "Login successfully";
            $data['register_response'] = "Registration successfull";
        }
    }
    return $data;
}

// Works per cat
function get_works_per_cat($cat, $return_links_arrays = false)
{
    global $con;

    $query = "SELECT * FROM `sd_works` WHERE `sd_work_cat` = '".$cat."'";

    $result = mysqli_query($con, $query);

    $limit = 0;

    $works_per_cat_res = "";

    while ($row = mysqli_fetch_assoc($result)) {

        if (getPostStatus($row['sd_work_id']) == 1) {

            $limit++;

            $sd_work_id = $row['sd_work_id'];

            $container = return_timeline_sd_work($sd_work_id);

            if (!empty($container)) {
                if ($return_links_arrays){
                    $works_per_cat_res .= base64_decode(unMaskData($row['sd_unique_work_id']));
                }else{
                    $works_per_cat_res .= $container;
                }
                
            }else{
                $limit--;
            }
        }

        if ($limit >= 4 ) {
            break;
        }
    }

    return $works_per_cat_res;
}


function appKeyToMail($app_key, $username)
{
    global $con;
    $query = "SELECT * FROM `sd_user_online_info` WHERE `user_online_info_app_key` = '".$app_key."' AND `user_online_info_name` = '".$username."'";
    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

            $email = $row['user_online_info_unq_id'];
    }else{
        $email = "";
    }

    return $email;
}

// View more work
function view_more_sd_work($cat_id)
{

    global $con;

    $random_conts = "";
    $order_conts = "";
    $cats_conts = "";

    if (!empty($cat_id)) {
        $random_conts .= get_works_per_cat($cat_id);
    }

    $query = 'SELECT * FROM `sd_works` ORDER BY RAND()';

    $result = mysqli_query($con, $query);

    $row = mysqli_fetch_assoc($result);

    $limit = 0;

    while ($row = mysqli_fetch_assoc($result)) {
    //
        $sd_work_id = $row['sd_work_id'];

        if (getPostStatus($sd_work_id) == 1) {

            $limit++;

            $container = return_timeline_sd_work($sd_work_id);

            if (!empty($container)) {
                $random_conts .= $container;
            }else{
                $limit--;
            }

            if ($limit > 10 ) {
                break;
            }
        }
    }

    $query = 'SELECT * FROM `sd_works` ORDER BY `sd_works`.`sd_work_id` DESC';

    $result = mysqli_query($con, $query);

    $limit = 0;

    while ($row = mysqli_fetch_assoc($result)) {

        $sd_work_id = $row['sd_work_id'];

        if (getPostStatus($sd_work_id) == 1) {

            $limit++;

            $sd_work_id = $row['sd_work_id'];

            $container = return_timeline_sd_work($sd_work_id);

            if (!empty($container)) {
                $order_conts .= $container;
            }else{
                $limit--;
            }

            if ($limit >10) {
                break;
            }

        }
    }


    $query = 'SELECT * FROM `sd_works` ORDER BY RAND() DESC';

    $result = mysqli_query($con, $query);

    $limit = 0;

    while ($row = mysqli_fetch_assoc($result)) {

        $sd_work_id = $row['sd_work_id'];

        if (getPostStatus($sd_work_id) == 1) {

            $limit++;

            $sd_work_id = $row['sd_work_id'];

            $container = return_timeline_sd_work($sd_work_id);

            if (!empty($container)) {
                $cats_conts .= $container;
            }else{
                $limit--;
            }

            if ($limit > 10) {
                break;
            }

        }
    }

    $cats_headers = "";

    $query = 'SELECT * FROM `sd_works_categories` ORDER BY RAND()';

    $result = mysqli_query($con, $query);

    while ($row = mysqli_fetch_assoc($result)) {

        $cat_id = $row['sd_work_cat_id'];
        $cat_name = unMaskData(base64_decode($row['sd_work_cat_name']));

        $cats_headers .= "<span data-id='$cat_id' class='work_cat_li'><a href='categories/$cat_id/#spinn_design_cat_works_cont'>$cat_name</a></span>";
    }




    $cont = "<div class='spinn_design_works_main_cont'>
        <div class='spinn_design_works_header'>
            <div class='spinn_design_works_header_cont boing' id='spinn_design_more_top_works_btn' data-target='spinn_design_more_top_works' style='box-shadow: 0 0 10px #ca0606' title='Top'>
                <i class='fas fa-bolt'></i>
            </div>
            <div class='spinn_design_works_header_cont boing' id='spinn_design_more_new_works_btn' data-target='spinn_design_more_new_works' title='new'>
                <i class='fas fa-plus-square'></i>
            </div>
            <div class='spinn_design_works_header_cont boing' id='spinn_design_more_cat_works_btn' data-target='spinn_design_more_cat_works' title='Categories'>
                <i class='fas fa-list'></i>
            </div>
        </div>

        <div class=''>
            <div class='spinn_design_works_sub_cont loading_more' id='spinn_design_more_top_works' data-orderby='random' data-category='sd_posts' data-requestedmore='false' data-maxReached='true'>
                <!-- Random -->
                $random_conts
            </div>
            <div class='spinn_design_works_sub_cont loading_more' id='spinn_design_more_new_works' style='display: none;' data-orderby='desc' data-category='sd_posts'  data-requestedmore='true'  data-maxReached='false'>
                <!-- Order -->
                $order_conts
            </div>
            <div class='spinn_design_works_sub_cont loading_more' id='spinn_design_more_cat_works' style='display: none;'>
                <div class='sd_cats_cont'>
                    <!-- cats headers -->
                    $cats_headers
                </div>
                <div class='loading_more' id='spinn_design_cat_works_cont' data-orderby='random' data-category='sd_posts' data-requestedmore='false'  data-maxReached='true' data-cat='' data-owner='' style='display: inline-block;'>
                    <!-- Cats -->
                    $cats_conts
                </div>
            </div>
        </div>
    </div>";

    return "<link rel='stylesheet' type='text/css' href='css/stories/sd_stories.css'><div>$cont</div>";
}

// Sd work preview side menu
function workPreviewSideMenu($sd_work_id)
{
    global $con;

    $more_from_user_cont = "<div class='sidebar right-bar no_propagation' id='work_preview_side_menu'>
    <ins class='adsbygoogle'
		style='display:block'
		data-ad-format='autorelaxed'
		data-ad-client='ca-pub-2317654314735642'
		data-ad-slot='1133508563'></ins>
	<script>
		(adsbygoogle = window.adsbygoogle || []).push({});
	</script>";
    $more_from_user = "";

    $id = base64_encode(maskData($sd_work_id));

    $query = "SELECT * FROM `sd_works` WHERE `sd_unique_work_id` = '".$id."'";

    $result = mysqli_query($con, $query);

    $limit = 0;

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
        $sd_work_owner = $row['sd_work_owner'];

        $query = "SELECT * FROM `sd_works` WHERE `sd_unique_work_id` != '".$row['sd_unique_work_id']."' AND `sd_work_owner` = '".$sd_work_owner."' ORDER BY RAND()";

        $result = mysqli_query($con, $query);

        if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
            $name = unMaskData(base64_decode(get_profile_details($row['sd_work_owner'])['first_name']));

            while ($row = mysqli_fetch_assoc($result)) {
                if (getPostStatus($row['sd_work_id']) == 1) {

                    $cat_id = unMaskData(base64_decode($row['sd_work_cat']));
                    $cat_name = unMaskData(base64_decode(get_cat_name($cat_id)));

                    if ($cat_name != "stories") {
                    
                        $limit++ ;
                        $ttle = unMaskData(base64_decode($row['sd_work_tittle']));
                        $un_id = unMaskData(base64_decode($row['sd_unique_work_id']));
                        $views = getSdWorkViews($row['sd_unique_work_id']);
                        $thumb = unMaskData(base64_decode($row['sd_work_thumb']));
                        $thumb = str_replace('SP_DES', "compressed_SP_DES", $thumb);
                        $thumb = str_replace('../', "", $thumb);
                        
                        if(!empty($thumb)){
							if (!file_exists($thumb) && !file_exists("../".$thumb)) {
								$thumb = "img/default/no_image.png";
							}
						}else{
							$thumb = "img/default/no_image.png";
						}

                        $post_date = relative_date(unMaskData(base64_decode($row['sd_work_date'])))." ago";

                        $more_from_user .= "<div class='side_menu_more_work'>
                            <div class='more_work_thumb'>
                                <a href='designs/$un_id'>
                                <img src='$thumb'>
                                </a>
                            </div>
                            <div class='more_work_ttle'>
                                $ttle
                            </div>
                            <div class='more_work_post_date'><i class='far fa-calendar-alt'></i> $post_date <i class='far fa-eye'></i> $views views</div>
                        </div> <div class='separator'></div>";
                    }
                }

                if ($limit > 5) {
                    break;
                }
            }

            if (!empty($more_from_user) && $more_from_user != "" && $more_from_user != " ") {
                $more_from_user = "<p>
                <i class='fas fa-plus-square'></i> More from $name
                </p>
                <div class='separator'></div>
                ".$more_from_user;
            }
        }
    

        if ($limit < 5) {
            $query = "SELECT * FROM `sd_works` WHERE `sd_unique_work_id` != '".$sd_work_id."' ORDER BY RAND()";

            $result = mysqli_query($con, $query);
            $you_might_like = "";

            if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
                $name = unMaskData(base64_decode(get_profile_details($row['sd_work_owner'])['first_name']));
                $limit = 0;
                while ($row = mysqli_fetch_assoc($result)) {
                    if (getPostStatus($row['sd_work_id']) == 1) {

                        $cat_id = unMaskData(base64_decode($row['sd_work_cat']));
                        $cat_name = unMaskData(base64_decode(get_cat_name($cat_id)));

                        if ($cat_name != "stories") {
                        
                            $limit++ ;
                            $ttle = unMaskData(base64_decode($row['sd_work_tittle']));
                            $un_id = unMaskData(base64_decode($row['sd_unique_work_id']));
                            $thumb = unMaskData(base64_decode($row['sd_work_thumb']));
                            $thumb = str_replace('SP_DES', "compressed_SP_DES", $thumb);
                            $thumb = str_replace('../', "", $thumb);
                            
                            if(!empty($thumb)){
                                if (!file_exists($thumb) && !file_exists("../".$thumb)) {
                                    $thumb = "img/default/no_image.png";
                                }
                            }else{
                                $thumb = "img/default/no_image.png";
                            }

                            $post_date = relative_date(unMaskData(base64_decode($row['sd_work_date'])))." ago";

                            $you_might_like .= "<div class='side_menu_more_work'>
                                <div class='more_work_thumb'>
                                    <a href='designs/$un_id'>
                                    <img src='$thumb'>
                                    </a>
                                </div>
                                <div class='more_work_ttle'>
                                    $ttle
                                </div>
                                <div class='more_work_post_date'>$post_date</div>
                            </div> <div class='separator'></div>";
                        }
                    }

                    if ($limit > 5) {
                        break;
                    }
                }

                if (!empty($you_might_like) && $you_might_like != "" && $you_might_like != " ") {
                    $more_from_user = $more_from_user."<h6>You Might Also Like</h6>".$you_might_like;
                }
            }
        }
    }

    $more_from_user .= "</div>";

    return $more_from_user_cont.$more_from_user;
}



function return_timeline_sd_work_preview($sd_work_id)
{
    global $con, 
    $my_email, 
    $tm, 
    $dbh, 
    $imageExtensions,
    $videoExtensions,
    $audioExtensions,
    $documentExtensions,
    $archiveExtensions,
    $dataExtensions,
    $vectorExtensions;

    $id = base64_encode(maskData($sd_work_id));

    $query = "SELECT * FROM `sd_works` WHERE `sd_unique_work_id` = '".$id."' OR `sd_work_id` = '".$sd_work_id."'";

    $result = mysqli_query($con, $query);

    $demo_imgs_cont = "";
    $attached_files = "";
    $other_files = "";
    $demo_vid_urls = array();

    if (isset($_SESSION['then_preview']) && ($_SESSION['then_preview'] === $sd_work_id || $_SESSION['then_preview'] === $id)){
        $_SESSION['then_preview'] = "";
    }

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

        $unq_id =  unMaskData(base64_decode($row['sd_unique_work_id']));

        if (getPostStatus($row['sd_work_id']) == 0) {
            $data['preview_job_res'] = "<br><br><h4 class='dynamic_margin'>We could not find what you are looking for. Contact us for more information.</h4>";
        }else{
            // UPDATE VIEWS
            $sql_vw = "INSERT INTO `sd_work_views`( 
            `sd_work_view_email`, 
            `sd_work_view_unq_id`, 
            `sd_work_view_date`)
                VALUES (
                :sd_work_view_email,
                :sd_work_view_unq_id,
                :sd_work_view_date)";

            $tm_vw = base64_encode(maskData($tm));

            $query_vw = $dbh->prepare($sql_vw);

            if (empty($my_email)) {
                $my_email = base64_encode(maskData(getUserIpAddr()));
            }

            $query_vw->bindParam('sd_work_view_email', $my_email, PDO::PARAM_STR );
            $query_vw->bindParam('sd_work_view_unq_id', $row['sd_unique_work_id'], PDO::PARAM_STR );
            $query_vw->bindParam('sd_work_view_date', $tm_vw, PDO::PARAM_STR );

            $query_vw->execute();
            // 

            $cat_id = unMaskData(base64_decode($row['sd_work_cat']));

            $cat_name = unMaskData(base64_decode(get_cat_name($cat_id)));

            $dwn = get_download_permission($row['sd_unique_work_id']);

            $doc_type = unMaskData(base64_decode($row['document_type']));

            if ($cat_name === "page") {

                if ($dwn !== "false") {
                    if ($dwn !== "true" && !empty($dwn)) {

                        $dwn = trim(unMaskData(base64_decode($dwn)));

                        $dwn_lnk = "<a href='$dwn' download=''><button class='default_button' onclick='$('.sd_popup_main_container').show()' style=''>Download Source Code < / > <i class='fas fa-edit'></i></button></a>";
                    }else{
                        $dwn_lnk = "<button class='default_button disabled' onclick='$('.sd_popup_main_container').show()'><a href='#' class='prev_job' data-id='$unq_id'>Download Source Code < / > <i class='fas fa-edit'></i></a></button>
                        <span class='more'>Can not be downloaded. Source file could not be found. If you are the page owner, please re-upload the <u><i><a href=?edit=$unq_id> Page zip file here</a></i></u></span>";
                    }
                }else{
                    $dwn_lnk = "<button class='default_button disabled' onclick='$('.sd_popup_main_container').show()'><a href='#' class='prev_job' data-id='$unq_id'>Download Source Code < / > <i class='fas fa-edit'></i></a></button> 
                    <span class='more'>The owner has not yet authorised direct downloads. Please contact the owner for a download link</span>";
                }

                $page_link = "<div class='spinn_design_work_page_link_cont'><button class='default_button'><a href='pages/$unq_id' target='_blank'>View Page <i class='fas fa-globe'></i></a></button> | $dwn_lnk</div>";
            }else{
                $page_link = get_cat_name($row['sd_work_cat']);
            }

            if ($cat_name === "poll") {
                $poll_cont = return_timeline_poll_cont($row['sd_work_link']);
            }else{
                $poll_cont = "";
            }

            $demo_imgs = unMaskData(base64_decode($row['sd_work_demos']));
            $demo_imgs = explode('XSPDX', $demo_imgs);

            $index = 0;

            if ($cat_name === "stories") {
                $demo_imgs_cont = "<div class='spinn_design_works_sub_cont'>".return_timeline_sd_work($row['sd_unique_work_id'])."</div>";
            }else{
                for ($i=0; $i < count($demo_imgs); $i++) {
                    if (!empty($demo_imgs[$i])) {


                        $ext = explode('.', $demo_imgs[$i]);
                        $ext = strtolower(end($ext));

                        if (in_array($ext, $imageExtensions)) {

                            $index++;

                            $demo_imgs[$i] = str_replace('SP_DES', "compressed_SP_DES", $demo_imgs[$i]);

                            $demo_imgs_cont = $demo_imgs_cont."<img class='work_demo_img' src='".$demo_imgs[$i]."'  data-preview='true' data-index='$index' data-post-id='$unq_id' data-group='work_demo_img'>";
                        }elseif (in_array($ext, $videoExtensions)) {
                            array_push($demo_vid_urls, $demo_imgs[$i]);
                        }elseif (in_array($ext, $archiveExtensions) || in_array($ext, $documentExtensions) || in_array($ext, $dataExtensions)) {
                            if ($dwn !== "false") {
                                if (isset($_SESSION['spinn_design_user'])) {
                                    if (in_array($ext, $archiveExtensions)){
                                        $attached_files .= "<button class='default_button' style=''>
                                        <a href='$demo_imgs[$i]' class='' data-id='$unq_id' download>
                                        Zip File 
                                        <i class='fas fa-download'></i>
                                        </a>";
                                    }
                                    if (in_array($ext, $documentExtensions)){
                                        $attached_files .= "<button class='default_button' style=''>
                                        <a href='$demo_imgs[$i]' class='' data-id='$unq_id' download>
                                        Document File 
                                        <i class='fas fa-download'></i>
                                        </a>";
                                    }
                                    if (in_array($ext, $dataExtensions)){
                                        $attached_files .= "<button class='default_button' style=''>
                                        <a href='$demo_imgs[$i]' class='' data-id='$unq_id' download>
                                        Data File 
                                        <i class='fas fa-download'></i>
                                        </a>";
                                    }
                                }else{
                                    $attached_files = "<a href='login?then=preview&key=$unq_id'><button><i class='fas fa-user-lock'></i> Login</button></a> or <a href='signup?then=preview&key=$unq_id'><button> <i class='fas fa-user-plus'></i> sign up  </button></a> to download these files.";
                                }
                            }else{
                                $attached_files = "<button class='default_button disabled' style=''><a href='#' class='' data-id='$unq_id'>
                                Download Attached Zip File 
                                <i class='fas fa-download'></i>
                                </a></button>  
                                <span class='more'>The attached zip file is not currently available for downloads. Please check back later.</span>";
                            }
                        }
                    }

                }
                if (!empty($demo_imgs_cont)) {
                    $demo_imgs_cont = "<div class='work_files'>
                    <h2><i class='far fa-image'></i> Images </h2>
                    <div class='work_more_demo_imgs_cont'>
                    <div class='work_more_demo_imgs'>
                                        ".
                                            $demo_imgs_cont."
                                    </div></div>
                                    </div>";
                }
            }

            if (!empty($attached_files)) {
                $other_files = "<div class='work_files'><h2><i class='fa-solid fa-file'></i></i> Attached Files</h2>
                <div class='other_attached_files'>
                $attached_files
                $page_link
                </div></div>";
            }


            $likes = getSdWorkLikes(base64_encode(maskData($row['sd_work_id'])));
            $views = getSdWorkViews($row['sd_unique_work_id']);
            $total_comments = getTotalCommentsByPostId($row['sd_unique_work_id']);

            if (getMyLike(base64_encode(maskData($row['sd_work_id'])))) {
                $like_class = "liked";
            }else{
                $like_class = "";
            }

            if (isset($_SESSION['spinn_design_user'])) {

                if ($_SESSION['spinn_design_user'] == $row['sd_work_owner']) {
                    $menu = "<li><i class='fas fa-solid fa-trash'></i> <a href='?delete=$unq_id'>Delete</a></li>
                        <li><i class='fas fa-edit'></i> <a href='?edit=$unq_id'>Edit</a></li>
                        ";
                    $story_menu = "<li><i class='fas fa-solid fa-trash'></i> <a href='?delete=$unq_id'>Delete</a></li>";
                }else{
                    $menu = "<li><i class='fas fa-solid fa-flag'></i> <a href='?report=$unq_id'>Report</a></li>";

                    $story_menu = "<li><i class='fas fa-solid fa-flag'></i> <a href='?report=$unq_id'>Report</a></li>";
                }


            }else{
                $menu = "<li><i class='fas fa-solid fa-flag'></i> <a href='?report=$unq_id'>Report</a></li>";

                $story_menu = "<li><i class='fas fa-solid fa-flag'></i> <a href='?report=$unq_id'>Report</a></li>";
            }

            $thumb = unMaskData(base64_decode($row['sd_work_thumb']));

            if (empty($thumb)) {
                $thumb = "img/default/no_image.png";
            }

            $row_profile = get_profile_details($row['sd_work_owner']);

            if (!empty($row_profile)) {
                $name = unMaskData(base64_decode($row_profile['first_name']))." ".unMaskData(base64_decode($row_profile['second_name']));
                $prof_link = unMaskData(base64_decode($row_profile['profile_link']));

                $prof_pic   = unMaskData(base64_decode($row_profile['prof_pic']));
                if (empty($prof_pic)) {
                    $prof_pic = "img/default/user.png";
                }else{
                    $prof_pic   = str_replace('compressed_SP_DES', "SP_DES", $prof_pic);
                }

                $cover_pic   = unMaskData(base64_decode($row_profile['cover_pic']));

                if (empty($cover_pic)) {
                    $cover_pic = get_random_cover_pic();
                }else{
                    $cover_pic = str_replace('compressed_SP_DES', "SP_DES", $cover_pic);
                }

                // Create stories container
                $q_stories = "SELECT * FROM `sd_stories` WHERE `sd_story_owner` = '".$row_profile['email_address']."' ORDER BY `sd_story_id` DESC";

                $stories = "";

                $r_stories = mysqli_query($con, $q_stories);
                if (mysqli_num_rows($r_stories) > 0) {

                    $stories = "<div class='work_stories'><div id='timeline_sd_status_cont_min'>
                    <div class='timeline_sd_status_cont_min'>";
                    while ($row_stories = mysqli_fetch_assoc($r_stories)) {
                        if (!empty(createMiniStoryContainer($row_stories))) {
                            // Concatenate stories
                            $stories .= createMiniStoryContainer($row_stories);
                        }
                    }

                    $stories .= "</div></div></div>";          

                }

            }else{
                $name = "Unknown";
                $prof_link = "";
                $prof_pic = "img/default/user.png";
                $cover_pic = get_random_cover_pic();
            }

            $post_date = relative_date(unMaskData(base64_decode($row['sd_work_date'])))." ago";

            $ttl = unMaskData(base64_decode($row['sd_work_tittle']));
            $desc = unMaskData(base64_decode($row['sd_work_desc']));

            // Horizontal ad;
            $query = "SELECT * FROM `sd_ads` ORDER BY RAND()";
            $result = mysqli_query($con, $query);
            $ad_count = 0;
            $ad_cont = "";

            while ($row = mysqli_fetch_assoc($result)) {
                $ad_count++;
                $ad_cont.="<span class='sd_horizontal_ad'>".unMaskData(base64_decode($row['sd_ad_link']))."</span>";

                if ($ad_count > 10) {
                    break;
                }
            }

            $vertical_ad = "
            <div id='sd_horizontal_ad_cont'>
                $ad_cont
            </div>";

            // Text only ad
            $text_only_ad = "
            <div id='sd_horizontal_ad_cont'>
                <div class='timeline_sd_status_cont_min timeline_ad_cont'>
                    <ins class='adsbygoogle'
                         style='display:block'
                         data-ad-format='fluid'
                         data-ad-layout-key='-fb+5w+4e-db+86'
                         data-ad-client='ca-pub-2317654314735642'
                         data-ad-slot='8140197327'></ins>
                    <script>
                         (adsbygoogle = window.adsbygoogle || []).push({});
                    </script>
                </div>  
            </div>";

            $personal_promo = "<div class='campaign_ad' style='
                background: var(--alt-background-color);'>
                    <img src='assets/images/campaign_ad.png' alt='ad'> 
            </div>";


            // ViewMore
            // $demo_imgs_cont = $demo_imgs_cont.view_more_sd_work($cat_id).workPreviewSideMenu($unq_id);

            $right_sidebar = workPreviewSideMenu($unq_id);
            $filename = '../include/left_sidebar.php'; 

            // Check if the file exists to avoid errors
            if (file_exists($filename)) {
                // Read the content of the file
                $left_sidebar = file_get_contents($filename);
            }else{
                $left_sidebar = file_get_contents('include/left_sidebar.php');;
            }

            $filename = '../include/social_links.php'; 

            // Check if the file exists to avoid errors
            if (file_exists($filename)) {
                // Read the content of the file
                $social_links = file_get_contents($filename);
            }else{
                $social_links = file_get_contents('include/social_links.php');;
            }


            if ($cat_name === "stories") {
                $data['preview_job_res'] = "$demo_imgs_cont";
            }else{
                if(isset($_SESSION['spinn_design_user'])){
                    $username = unMaskData(base64_decode(get_profile_details($_SESSION['spinn_design_user'])['profile_link']));
                }else{
                    $username = "";
                }
                
                $data['username'] = $username;

                $data['preview_job_res'] = "
                    <div class='container'>
                        $left_sidebar
                        <div class='content work_header' id='main-work-content' data-id='$sd_work_id' data-username='$username'>
                            <div class='mini_profile_cont'>					
                                <div class='mini_profile_pics' style='--before-bg-image:url(../$cover_pic)'>
                                    <div class='mini_profile_cover_pic'>
                                        <img src='$cover_pic' alt='cover picture'>
                                    </div>
                                    <div class='mini_profile_pic_name'>
                                        <a href='?profile=$prof_link'>
                                            <span class='mini_profile_pic'>
                                                <img src='$prof_pic' alt='profile picture'>
                                            </span>
                                            <span class='mini_profile_name'>$name</span>
                                        </a>
                                        $social_links
                                        <button class='spinn_design_work_more_menu'>
                                            <i class='fas fa-ellipsis-v'></i>
                                            <ul>
                                                $menu
                                            </ul>
                                        </button>

                                    </div>
                                </div>
                                
                            </div>
                            <div class='work_ttl_cont'>
                                <div class='post_inf'>
                                    <div class='work_ratings'>
                                        <p><i class='far fa-calendar-alt'></i> $post_date | </i> $views views</p>
                                    </div>
                                    <div class='work_ratings'>
                                        <button class='like_job boing $like_class' data-id='$unq_id'>
                                            <span class='likes_count boing' data-id='$unq_id'>$likes </span>
                                            <i class='fas fa-thumbs-up'></i>
                                        </button>
                                        <button id='comment_job'>
                                            <span class='comment_job boing' data-id='$unq_id' title='Comment'>
                                            $total_comments <i class='fas fa-comments'></i> 
                                            </span>
                                        </button>
                                        <button class='share_work cb boing' data-share-work-id='$unq_id'>
                                            <i class='fas fa-share-alt-square'></i> 
                                        </button>
                                    </div>
                                </div>
                            </div>
                            <div id='raw_desc' style='display: none !important'>$desc</div>
                            <div class='work_description' data-cat='$cat_name' id='work_description'>
                                <p class='work_ttl'>$ttl</p>
                                <div id='desc' class='markdown-content markdown' data-doc-type=$doc_type>$desc</div>
                            </div>
                            
                            $other_files
                            
                            $text_only_ad
                            $poll_cont
                            <div class='work_files'>
                                <div class='sd_videos'></div>
                            </div>
                            $demo_imgs_cont
                            $stories
                        </div>
                        $right_sidebar
                    </div>
                        
                        ";
            }

            $data['demo_vid_urls'] = $demo_vid_urls;
            // $data['right_sidebar'] = $right_sidebar;

        }
    }

    $data['job_id'] = $sd_work_id;
    $data['doc_type'] = $doc_type;

    return $data;
}

function get_download_permission($id)
{
    global $con;

    $source_file = "";

    $sql = "SELECT * FROM `sd_work_filee_download_status` WHERE `sd_work_id`= '".$id."'";
    $result = mysqli_query($con, $sql);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

        if (!empty($row['sd_work_source_file'])) {
            $source_file = $row['sd_work_source_file'];
        }

        if (unMaskData(base64_decode($row['sd_work_file_download_status'])) === "all") {
            if (!empty($source_file)) {
                return $source_file;
            }else{
                return "true";
            }

        }else if (isset($_SESSION['spinn_design_user'])) {
            $sql = "SELECT * FROM `sd_works` WHERE `sd_unique_work_id` = '".$id."'";
            $result = mysqli_query($con, $sql);
            if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
                if ($_SESSION['spinn_design_user'] == $row['sd_work_owner']) {
                    if (!empty($source_file)) {
                        return $source_file;
                    }else{
                        return "true";
                    }
                }else{
                    return "false";
                }
            }else{
                return "false";
            }

        }else{
            return "false";
        }
    }else if (isset($_SESSION['spinn_design_user'])) {
        $sql = "SELECT * FROM `sd_works` WHERE `sd_unique_work_id` = '".$id."'";
        $result = mysqli_query($con, $sql);
        if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
            if ($_SESSION['spinn_design_user'] == $row['sd_work_owner']) {
                return "true";
            }else{
                return "false";
            }
        }else{
            return "false";
        }
    }else{
        return "false";
    }
}


// /////////////
// Sd media browser
function get_new_size($sizes)
{
    //global $sizes;
    $get_size = $sizes[array_rand($sizes, 1)];
    if ($get_size !== "large") {
        return $get_size;
    }else{
        get_new_size($sizes);
    }
}

// timeline poll cont
function return_timeline_poll_cont($enc_uniqueId)
{
    global $con, $my_email;

    $cont = "";

    $query = "SELECT * FROM `sd_polls` WHERE `sd_poll_unique_id` = '".$enc_uniqueId."'";

    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
        $sd_poll_quiz = unMaskData(base64_decode($row['sd_poll_quiz']));
        $sd_poll_options = unMaskData(base64_decode($row['sd_poll_options']));
        $sd_poll_date = unMaskData(base64_decode($row['sd_poll_date']));
        $id = unMaskData(base64_decode($row['sd_poll_unique_id']));

        $query1 = "SELECT * FROM `sd_poll_votes` WHERE `sd_poll_vote_unique_id` = '".$enc_uniqueId."' AND `sd_poll_voter` = '".$my_email."'";
        $result1 = mysqli_query($con, $query1);
        if ($row1 = mysqli_fetch_assoc($result1)) {
            $my_vote = unMaskData(base64_decode($row1['sd_poll_vote_option']));
        }else{
            $my_vote = "";
        }

        if ($row['sd_poll_owner'] === $my_email) {
            $more_menu = "<button class='spinn_design_work_more_menu'>
                    <i class='fas fa-ellipsis-v'></i>
                    <ul>
                        <li>
                            <a href='?deletepoll=$id'><i class='fas fa-solid fa-trash'></i> Delete Poll</a>
                        </li>
                    </ul>
                </button>";
        }else{
            $more_menu = "";
        }

        $sd_poll_options =  explode("XSPDESX", $sd_poll_options);
        $options = "";
        foreach ($sd_poll_options as $key => $value) {
            if (!empty($value) && $value != " ") {
                if (!empty($my_vote) && $my_vote === $value) {
                    $options .= "<button class='sd_timeline_poll_opt sd_polls_option_btn sd_polls_active_option' data-val='$value' data-id='$id'>$value</button>";
                }else{
                    $options .= "<button class='sd_timeline_poll_opt sd_polls_option_btn' data-val='$value' data-id='$id'>$value</button>";
                }
            }
        }

        $sd_poll_summary = pollVotesSummary($enc_uniqueId);
        $sd_poll_graph = createPollgraph($enc_uniqueId);

        $cont = "<div class='sd_timeline_poll_cont'>

                $more_menu

                <div class='sd_timeline_poll_quiz'>
                    <div class='sd_polls_statement'>
                        <p>
                            $sd_poll_quiz
                        </p>
                    </div>
                </div>
                <div class='sd_timeline_poll_opts_cont'>
                    <button class='default_button vote_sd_poll no_propagation'><i class='fa-solid fa-check-to-slot'></i> Vote for this poll</button>
                    <div class='sd_timeline_poll_opts sd_polls_options no_propagation'>
                        $options
                    </div>
                </div>
                <div class='sd_timeline_poll_results_cont'>
                    <button class='view_sd_polls_results default_button no_propagation'><i class='fa-solid fa-square-poll-horizontal'></i> View Poll Results</button>
                    <div class='sd_polls_results no_propagation' data-id='$id' style='display: none;'>
                        <div class='sd_polls_summary_cont'>
                            $sd_poll_summary
                        </div>
                        <div class='' id='sd_polls_main_graph_prev_cont'>
                            <div class='sd_polls_graph_cont' data-create-index='true'>
                                $sd_poll_graph
                            </div>
                        </div>
                    </div>
                </div>
            </div>";
    }

    return $cont;
}

// poll votes summary
function pollVotesSummary($enc_uniqueId)
{
    global $con, $my_email;
    $summary = "";

    $query = "SELECT * FROM `sd_polls` WHERE `sd_poll_unique_id` = '".$enc_uniqueId."'";
    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {

        $sd_poll_options = unMaskData(base64_decode($row['sd_poll_options']));

        $sd_poll_options =  explode("XSPDESX", $sd_poll_options);
        $options = "";
        foreach ($sd_poll_options as $key => $value) {
            if (!empty($value) && $value != " ") {
                $enc_opt = base64_encode(maskData($value));

                $query1 = "SELECT * FROM `sd_poll_votes` WHERE `sd_poll_vote_unique_id` = '".$enc_uniqueId."' AND `sd_poll_vote_option` = '".$enc_opt."'";
                $result1 = mysqli_query($con, $query1);
                $total_opt_votes = mysqli_num_rows($result1);
                $options .= "<div>".$value.": <span>".$total_opt_votes."</span></div>";
            }
        }

        $query = "SELECT * FROM `sd_poll_votes` WHERE `sd_poll_vote_unique_id` = '".$enc_uniqueId."' AND `sd_poll_voter` = '".$my_email."'";
        $result = mysqli_query($con, $query);
        if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
            $my_vote = unMaskData(base64_decode($row['sd_poll_vote_option']));
        }else{
            $my_vote = "Please Vote <i class='fa-solid fa-check-to-slot'></i> Above <i class='fa-solid fa-hand-point-up'></i>";
        }

        $my_vote = "<div>My Vote <i class='fa-solid fa-check-to-slot'></i>: <span>$my_vote</span></div>";

        $query = "SELECT * FROM `sd_poll_votes` WHERE `sd_poll_vote_unique_id` = '".$enc_uniqueId."'";
        $result = mysqli_query($con, $query);
        if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
            $total_votes = mysqli_num_rows($result);
        }else{
            $total_votes = 0;
        }

        $total_votes = "<div>Total Votes <i class='fas fa-poll'></i>: <span>$total_votes</span></div>";

        $summary = $my_vote.$total_votes.$options;
    }

    return $summary;
}

// poll graphs
function createPollgraph($enc_uniqueId)
{
    global $con, $my_email;
    $graph = "";

    $query = "SELECT * FROM `sd_polls` WHERE `sd_poll_unique_id` = '".$enc_uniqueId."'";
    $result = mysqli_query($con, $query);

    if (!is_bool($result) && $row = mysqli_fetch_assoc($result)) {
        $sd_poll_options = unMaskData(base64_decode($row['sd_poll_options']));
        $sd_poll_options =  explode("XSPDESX", $sd_poll_options);
        $options = 0;
        foreach ($sd_poll_options as $key => $value) {
            if (!empty($value) && $value != " ") {
                $options++;
            }
        }
        $graph_type = unMaskData(base64_decode($row['sd_poll_graph']));

        $query = "SELECT * FROM `sd_poll_votes` WHERE `sd_poll_vote_unique_id` = '".$enc_uniqueId."'";
        $result = mysqli_query($con, $query);
        $total_votes = mysqli_num_rows($result);

        if ($graph_type == "bar") {

            foreach ($sd_poll_options as $key => $value) {
                if (!empty($value) && $value != " ") {
                    $enc_opt = base64_encode(maskData($value));
                    $query1 = "SELECT * FROM `sd_poll_votes` WHERE `sd_poll_vote_unique_id` = '".$enc_uniqueId."' AND `sd_poll_vote_option` = '".$enc_opt."'";
                    $result1 = mysqli_query($con, $query1);
                    $total_opt_votes = mysqli_num_rows($result1);
                    if ($total_votes == 0 || $total_opt_votes == 0) {
                        $perc_val = 0;
                    }else{
                        $perc_val = ( $total_opt_votes / $total_votes) * 100;
                    }


                    $graph .= "<div class='sd_polls_graph' data-label='$value' style='width: $perc_val%;'></div>";
                }
            }
        }
    }

    return $graph;
}
function get_random_cover_pic() {
    // Define an array of cover picture strings (URLs or file paths)
    $coverPics = [
        'img/bg/luca-bravo-XJXWbfSo2f0-unsplash.jpg',
        'img/bg/3303176.jpg',
        'img/bg/233568.jpg',
        'img/bg/333567.jpg',
        'img/bg/1554201.jpg',
        'img/bg/1980184.jpg',
        'img/bg/2196384.jpg',
        'img/bg/2434040.jpg',
        'img/bg/3102870.jpg',
        'img/bg/3303179.jpg',
        'img/bg/3303181.jpg',
        'img/bg/3303182.jpg',
        'img/bg/3303195.jpg',
        'img/bg/3303198.jpg',
        'img/bg/3303199.jpg',
        'img/bg/3303200.jpg'
    ];

    // Get a random index from the array
    $randomIndex = array_rand($coverPics);

    // Return the randomly selected cover picture string
    return $coverPics[$randomIndex];
}

function getTotalCommentsByPostId($post_id) {
    global $dbh; // Use the global database connection

    // Prepare the SQL query to count comments for the given post_id
    $sql = "SELECT COUNT(*) AS total_comments FROM sd_comments WHERE post_unique_id = :post_id";

    $stmt = $dbh->prepare($sql); // Prepare the statement
    $stmt->bindParam(':post_id', $post_id, PDO::PARAM_STR); // Bind the post_id parameter

    // Execute the query
    $stmt->execute();

    // Fetch the result
    $result = $stmt->fetch(PDO::FETCH_ASSOC);

    // Return the total comments count
    return $result['total_comments'];
}

function truncateText($text, $limit) {
    // Check if the text length exceeds the limit
    if (strlen($text) > $limit) {
        // Truncate the text and add ellipsis
        return substr($text, 0, $limit) . '...';
    }
    // Return the original text if it's within the limit
    return $text;
}


$prof_pic = "";
$prof_cover = "";

// Logged profile
if (isset($_SESSION['spinn_design_user'])) {
    $my_email = $_SESSION['spinn_design_user'];
    $row_profile = get_profile_details($my_email);

    $my_unq_id = $row_profile['profile_link'];
    if (!empty($row_profile)) {
    	$prof_name = unMaskData(base64_decode($row_profile['first_name']))." ".unMaskData(base64_decode($row_profile['second_name']));
    	$prof_pic = unMaskData(base64_decode($row_profile['prof_pic']));
    	$prof_cover = unMaskData(base64_decode($row_profile['cover_pic']));
    	$prof_email = unMaskData(base64_decode($row_profile['email_address']));
    	
    	$prof_pic = str_replace('SP_DES', "compressed_SP_DES", $prof_pic);
    	$prof_cover = str_replace('SP_DES', "compressed_SP_DES", $prof_cover);

    	$profile_link = unMaskData(base64_decode($row_profile['profile_link']));
    	$profile_bio = unMaskData(base64_decode($row_profile['bio']));
    	$profile_other_links = unMaskData(base64_decode($row_profile['other_links']));
    	$profile_phone = unMaskData(base64_decode($row_profile['phone_number']));

    	
    }
}else{
    $my_email = "";
    $my_unq_id = "";
}

if (empty($prof_pic) || $prof_pic == "updaters/") {
    $prof_pic = "img/default/user.png";
}
if (empty($prof_cover) || $prof_cover == "updaters/") {
    $prof_cover = get_random_cover_pic();
}

// Set cookies
if (!isset($_COOKIE['user_id'])) {
    // Generate a unique identifier for the user
    $unique_user_id = base64_encode(maskData(uniqid('user_', true)));
    
    // Set a cookie for 10 years
    setcookie('user_id', $unique_user_id, time() + (10 * 365 * 24 * 60 * 60), "/");
} else {
    $unique_user_id = $_COOKIE['user_id'];
}

?>