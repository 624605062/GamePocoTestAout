from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import poco
from poco.drivers.unity3d import UnityPoco
class MainPage:
    #poco=AndroidUiautomationPoco(use_airtest_input=True,screenshot_each_action=False)
    poco=UnityPoco(use_airtest_input=True,screenshot_each_action=False)