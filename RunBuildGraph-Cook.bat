echo %~dp0
set CurPath=%~dp0
set UATPath=F:/UE5/UE_Src/UE_5.3_T3/Engine/Build/BatchFiles/
set BuildGraphPath=E:/WorkPlace/WP_YXK/ue5_build_graph_demo/Tools/BuildGraph.xml
%UATPath%RunUAT.bat BuildGraph -Script=%BuildGraphPath% -ProjectRoot=E:/WorkPlace/WP_YXK/ue5_build_graph_demo -UProjectPath=E:/WorkPlace/WP_YXK/ue5_build_graph_demo/FirstPersonGame.uproject -Target="Windows Cook" -StageDirectory="E:\WorkPlace\WP_YXK\ue5_build_graph_demo\dist" -NoP4 -WriteToSharedStorage -BuildMachine > Cook.Log
pause