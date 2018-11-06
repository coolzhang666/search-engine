import BF
import KMP


if __name__ == "__main__":
    file = open("test.txt")
    try:
        text_string = file.read()
    finally:
        file.close()
    pat_string = "bacbababadababacambabacaddababacasdsd"

    print(KMP.kmp_search(text_string, pat_string))

    print("*" * 50)

    print(BF.bf_search(text_string, pat_string))
