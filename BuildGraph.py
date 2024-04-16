import sys
import os

def main(argv):
    ProjectName             = "FirstPersonGame"
    ProjectRoot             = r"E:/WorkPlace/WP_YXK/ue5_build_graph_demo/"
    UProjectPath            = r"E:/WorkPlace/WP_YXK/ue5_build_graph_demo/FirstPersonGame.uproject"
    StageDirectory          = r"E:\WorkPlace\WP_YXK\ue5_build_graph_demo\dist"
    Platform                = "Android"
    ClientConfig            = "Development"
    OutputDir               = r"E:/WorkPlace/WP_YXK/ue5_build_graph_demo/PakOutput"
    SkipBuildProject        = "true"
    SkipBuildEditor         = "true"
    Unrealexe               = r"D:\WP_YXK\UE\UE_5.3\Engine\Binaries\Win64\UnrealEditor-Cmd.exe "
    EditorIOPort            = "54689"
    TargetName              = r"Windows Pak and Stage"

    cmd = f"-set:ProjectName={ProjectName} -set:ProjectRoot={ProjectRoot} -set:UProjectPath={UProjectPath} -set:StageDirectory={StageDirectory}"

    fileDir     = r"D:/WP_YXK/UE/UE_5.3/Engine/Build/BatchFiles/RunUAT.bat"
    target      = "Windows Pak And Stage"
    script      = r"E:\WorkPlace\WP_YXK\ue5_build_graph_demo\Tools\BuildGraph.xml"

    cmd = f"{fileDir} BuildGraph -Script={script} -Target={target} {cmd}"

    print(f"cmd: {cmd}")

    ret = os.system(cmd)

    if ret == 0:
        print(f"run build ret val = {ret}")
    else:
        raise Exception("project build faild!")
        pass


if __name__ == "__main__":
    main(sys.argv[1:])
    input("press any to close")