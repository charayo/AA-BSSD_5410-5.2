# Original code accessed on: 2/22/22; from:
# https://www.geeksforgeeks.org/longest -common-subsequence-dp-4/
# This code is contributed by Nikhil Kumar Singh (nickzuck_007)
# Dynamic Programming implementation of LCS problem

def read_txt(fname, enc):
    with open(fname, 'r', encoding=enc) as file:
        texts = file.read()  # read file
    return texts  # return texts in file
# end def read_txt(fname, enc):


def number_of_Char(text):
    return len(text)


def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[o..¡-1] and Y[o..¡-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    # L[m] [n] contains the length of LCS of X[o..n-1] & Y[O..m-1]
    return L[m][n]
# end of function lcs


def main():
    # Driver program to test the above function
    X = "AGGTAB"
    Y = "GXTXAYB"

    code_before_edit = read_txt("code_before.txt", "utf-8")
    code_after_edit = read_txt("code_after.txt", "utf-8")
    source_char_len = number_of_Char(code_before_edit)
    final_char_len = number_of_Char(code_after_edit)
    print("Number of duplicate characters is: ", lcs(code_before_edit, code_after_edit))
    print("Number of character present in the Code copied from online source is:", source_char_len)
    print("Number of character present in the modified code is:", final_char_len)
    print("The amount of changes made in character to the code copied is:", (final_char_len - source_char_len))

# end def main()


if __name__ == "__main__":
    main()
