echo %~dp0
set CurPath=%~dp0
set UATPath=F:/UE5/UE_Src/UE_5.3_T3/Engine/Build/BatchFiles/
%UATPath%RunUAT.bat BuildGraph -Script=%CurPath%Tools/BuildGraph.xml -ProjectRoot="E:/WorkPlace/WP_YXK/ue5_build_graph_demo" -UProjectPath="E:/WorkPlace/WP_YXK/ue5_build_graph_demo/FirstPersonGame.uproject" -Target="Windows Build" -StageDirectory="E:\WorkPlace\WP_YXK\ue5_build_graph_demo\dist" -NoP4 -WriteToSharedStorage -BuildMachine > Build.Log
pause