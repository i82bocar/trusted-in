from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCharts import QChartView, QPieSeries, QChart, QPieSlice
from PySide6.QtGui import QPainter, QColor, QBrush, QPen, QFont
from PySide6.QtCore import Qt

class DonutChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set transparent background for the widget
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet("background: transparent;")

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.chartView = QChartView()
        self.chartView.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.chartView.setStyleSheet("background: transparent; border: none;")
        self.layout.addWidget(self.chartView)

        # Create series and chart
        self.series = QPieSeries()
        self.series.setPieSize(0.7)  # Make the donut smaller within the view
        
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setBackgroundBrush(QBrush(Qt.GlobalColor.transparent))
        self.chart.setTitle("Vault Item Types")
        
        # Dark theme colors
        dark_color = QColor(45, 45, 45)
        text_color = QColor(220, 220, 220)
        self.chart.setTitleBrush(QBrush(text_color))
        
        # Configure legend
        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.chart.legend().setLabelColor(text_color)
        self.chart.legend().setBackgroundVisible(False)
        self.chart.legend().setFont(QFont("Arial", 8))
        
        # Configure chart appearance
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        self.chart.setBackgroundRoundness(0)
        # self.chart.setMargins(0)
        
        # Set transparent background for plot area
        self.chart.setPlotAreaBackgroundBrush(QBrush(Qt.GlobalColor.transparent))
        self.chart.setPlotAreaBackgroundVisible(True)
        
        self.chartView.setChart(self.chart)

    def updateData(self, data: dict):
        """data: {'Passwords': 5, 'Contacts': 3, ...}"""
        self.series.clear()
        total = sum(data.values())
        if total == 0:
            return

        # Dark theme slice colors
        colors = [
            QColor(65, 105, 225),   # Royal Blue
            QColor(50, 205, 50),    # Lime Green
            QColor(255, 140, 0),     # Dark Orange
            QColor(138, 43, 226),    # Blue Violet
            QColor(220, 20, 60),     # Crimson
            QColor(0, 206, 209)      # Dark Turquoise
        ]

        for i, (label, value) in enumerate(data.items()):
            if value > 0:
                slice = self.series.append(f"{label} ({value})", value)
                slice.setLabelVisible(True)
                slice.setLabelColor(QColor(220, 220, 220))
                slice.setLabelFont(QFont("Arial", 8))
                slice.setBrush(colors[i % len(colors)])
                slice.setBorderColor(QColor(45, 45, 45))
                slice.setBorderWidth(1)

        self.series.setHoleSize(0.5)
        self.series.setLabelsPosition(QPieSlice.LabelPosition.LabelOutside)
        
        # Configure pie slice labels
        for slice in self.series.slices():
            slice.setLabelArmLengthFactor(0.1)
            slice.setExploded(False)
            slice.setLabelVisible(True)