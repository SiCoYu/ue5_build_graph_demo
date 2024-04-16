echo %~dp0
set CurPath=%~dp0
set UE5UATPath=D:/WP_YXK/UE/UE_5.3/Engine/Build/BatchFiles/
rem F:/UE5/UE_Src/UE_5.3_T3/Engine/Build/BatchFiles/

%UE5UATPath%RunUAT.bat BuildGraph -Script=%CurPath%Tools/BuildGraph.xml  -Target="Windows Pak And Stage" -set:UATPath=%UE5UATPath%RunUAT.bat -set:ProjectRoot="E:/WorkPlace/WP_YXK/ue5_build_graph_demo" -set:UProjectPath="E:/WorkPlace/WP_YXK/ue5_build_graph_demo/FirstPersonGame.uproject" -set:StageDirectory="E:\WorkPlace\WP_YXK\ue5_build_graph_demo\PakOutputV2" -NoP4 -WriteToSharedStorage -BuildMachine > Pak.Log
pause