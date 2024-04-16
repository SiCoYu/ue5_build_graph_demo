import sys
import os

def main(argv):
    ProjectName             = "FirstPersonGame"
    ProjectDir              = r"E:/WorkPlace/WP_YXK/ue5_build_graph_demo/"
    Platform                = "Android"
    ClientConfig            = "Development"
    OutputDir               = r"E:/WorkPlace/WP_YXK/ue5_build_graph_demo/PakOutput"
    SkipBuildProject        = "true"
    SkipBuildEditor         = "true"
    Unrealexe               = r"D:\WP_YXK\UE\UE_5.3\Engine\Binaries\Win64\UnrealEditor-Cmd.exe "
    EditorIOPort            = "54689"

    cmd = f"-set:ProjectName={ProjectName} -set:ProjectDir={ProjectDir} -set:Platform={Platform}" \
            f" -set:ClientConfig={ClientConfig} -set:OutputDir={OutputDir} -set:SkipBuildProject={SkipBuildProject}" \
                f" -set:SkipBuildEditor={SkipBuildEditor} -set:Unrealexe={Unrealexe} -set:EditorIOPort={EditorIOPort}"


    fileDir     = r"D:/WP_YXK/UE/UE_5.3/Engine/Build/BatchFiles/RunUAT.bat"
    target      = "MyBuild"
    script      = r"E:\WorkPlace\WP_YXK\ue5_build_graph_demo\Tools\Build.xml"

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