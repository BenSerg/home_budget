from create_widgets_functions import *
from window_functions import *
import matplotlib.pyplot as plt


class GraphWindow(QWidget):
    def return_to_parent_window(self):
        self.parent.show()
        self.close()

    def __init__(self, parent: QWidget, data_y, data_x):
        super().__init__()
        self.return_button = None
        self.data_x = data_x
        self.data_y = data_y
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('График')
        set_window_geometry(self)
        from budget_change_window import BudgetChange
        from amount_window import AmountWindow
        from financial_threads_window import FinancialThreads
        if self.parent.__class__ == BudgetChange:
            plt.figure()
            plt.plot(self.data_y, [i[0] for i in self.data_x], color='red', label='Расход', marker='.', markersize=20)
            plt.plot(self.data_y, [i[1] for i in self.data_x], color='green', label='Приход', marker='.', markersize=20)
        elif self.parent.__class__ == AmountWindow:
            plt.figure()
            plt.plot(self.data_y, self.data_x, color='blue', label='Прибыль', marker='.', markersize=20)
        elif self.parent.__class__ == FinancialThreads:
            plt.figure()
            plt.bar(self.data_x, self.data_y, color='yellow', edgecolor='black', alpha=0.5)
            plt.grid(axis='x')
        else:
            plt.figure()
            plt.plot(self.data_y, self.data_x, color='purple', label='Соотношение Приход/Расход', marker='.', markersize=20)
        plt.xticks(rotation=25)
        plt.grid()
        plt.legend()
        plt.savefig('plot.png')
        plt_label = QLabel(self)
        plot_pixmap = QtGui.QPixmap('plot.png')
        plt_label.setPixmap(plot_pixmap)
        plt_label.setGeometry(100, 25, 750, 600)
        font = create_font(size=41)
        font.setBold(True)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_parent_window)
