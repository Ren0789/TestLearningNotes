@echo off
::���ð�����APK·��(�鿴AndroidӦ�ð�����Activity�ļ�������-http://blog.csdn.net/jlminghui/article/details/40622103)
set app_pkg=com.che168.ucdealer
set app_aty=com.che168.ucdealer.activity.LaunchActivity
::set app_apk=C:\Users\renyi0301\Desktop\chezhiying_beta.apk
set app_apk=.\chezhiying_beta.apk

::�鿴�Ƿ��Ѱ�װ
adb shell pm list package | findstr %app_pkg% > temp.txt
set /p pkg=<temp.txt
del temp.txt
echo %pkg%
::�����װ�˾�ж��
if "%pkg%"=="package:%app_pkg%" adb uninstall %app_pkg%
::ж�غ��ٴΰ�װ
adb install %app_apk%
::��ӡ��ִ����ɱ�־
echo Install Over!

::����APP
adb shell am start -n %app_pkg%/%app_aty%
::��ӡ��ִ����ɱ�־
echo Start Over!

::�ȴ�3���ر�(cmd-bat������������ʱ����-http://blog.csdn.net/xie1xiao1jun/article/details/45876815)
@choice /t 3 /d y /n >nul