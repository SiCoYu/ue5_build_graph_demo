echo %~dp0
set CurPath=%~dp0
set UATPath=F:/UE5/UE_5.3_T3/Engine/Build/BatchFiles/

%UATPath%RunUAT.bat BuildGraph -Script=%CurPath%Tools/BuildGraph.xml -set:ProjectRoot="F:/Git_WP/UE_YXK/WP_YXK/ue5_build_graph_demo" -set:UProjectPath="F:/Git_WP/UE_YXK/WP_YXK/ue5_build_graph_demo/FirstPersonGame.uproject" -Target="Windows Build" -set:StageDirectory="F:/Git_WP/UE_YXK/WP_YXK/ue5_build_graph_demo/dist" -NoP4 -WriteToSharedStorage -BuildMachine > Build.Log
pause