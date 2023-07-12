from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
import random

from ui import Ui_Dialog


class Controller(QWidget, Ui_Dialog):
    def __init__(self):
        super(Controller, self).__init__()  # （子类的类名，子类的实例） 通过.__init__()来初始化父辈的构造函数，即QWidget, Ui_IICAutoTest
        self.setupUi(self)  # 这个方法是由Qt Designer生成的Ui_IICAutoTest类中的一个函数，用于设置和初始化UI界面。
        self.pushButton.clicked.connect(self.buttonClicked)
        self.timer = QTimer()
        self.timer.timeout.connect(self.looping)
        self.timer.start(1000)  # 每隔1秒触发一次timeout信号

    def buttonClicked(self):
        # QtWidgets.QMessageBox.warning(self, '1087X', "6月22日凌晨1时许，福州交警在连江北路开展夜查行动时，一辆车牌号为闽C5F43F的小车因涉嫌非法改装，被交警当场拦下。",
        #                               QtWidgets.QMessageBox.Yes)
        self.timer.stop()
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('1087X')
        msg_box.setText("6月22日凌晨1时许，福州交警在连江北路开展夜查行动时，一辆车牌号为闽C5F43F的小车因涉嫌非法改装，被交警当场拦下。")

        # 添加自定义按钮
        custom_button = msg_box.addButton("罚款500元并打印罚单", QtWidgets.QMessageBox.YesRole)

        # 连接自定义按钮的点击事件
        custom_button.clicked.connect(self.customButtonClicked)

        msg_box.exec()

    def looping(self):
        self.moveButton()
        self.show()

    def moveButton(self):
        # 生成随机的按钮位置
        x = random.randint(0, self.width() - self.pushButton.width())
        y = random.randint(0, self.height() - self.pushButton.height())
        self.pushButton.move(x, y)


    def customButtonClicked(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, '福州交警电子罚单', '', 'Text Files (*.txt)')
        # QtWidgets.QFileDialog.getSaveFileName 是一个静态方法，用于显示文件保存对话框并获取用户选择的文件名。
        # Text Files (*.txt)是文件过滤器，用于限制用户可以选择的文件类型，并将其放置到前面_
        if file_name:
            with open(file_name, 'w') as txt_file:  # 'w'打开文件的模式，这里是以写入模式打开文件。
                txt_file.write(f"道路交通安全违法行为处理通知书\n")
                txt_file.write(f"当事人联\n")
                txt_file.write("\n")
                txt_file.write(f"编号:4420106901363695\n")
                txt_file.write(f"当事人:柯x宏\n")
                txt_file.write(f"准驾车型：C1\n")
                txt_file.write(f"驾驶车辆：小型汽车\n")
                txt_file.write(f"发证机关:福建省福州市公安局交通巡逻警察支队车辆管理所\n")
                txt_file.write("\n")
                txt_file.write(f"当事人驾驶牌号为闽C5F43F车辆类型为小型轿车的机动车，\n")
                txt_file.write(f"于2023年6月22日凌晨1时23分，在连江北路，实施\n")
                txt_file.write(f"擅自改变机动车外形和已登记的有关技术参数的违法行为\n")
                txt_file.write(f"(代码10871)，法律依据:《中华人民共和国道路交通安全法》\n")
                txt_file.write(f"第十六条第一项。要求于15日内携带机动车行驶证、机动车驾\n")
                txt_file.write(f"驶证，到福州市鼓楼区西二环北路181号福州市通警察\n")
                txt_file.write(f"支队鼓楼大队服务窗口接受处理。\n")


            TicketCompleted = QtWidgets.QMessageBox()
            TicketCompleted.setWindowTitle('罚单已开具')
            TicketCompleted.setText(f"福州交警提醒您：马路不是赛车场\n" + "行车不规范，亲人泪两行")
            TicketCompleted.addButton(QtWidgets.QMessageBox.Ok)
            TicketCompleted.exec()

            self.timer.start()
