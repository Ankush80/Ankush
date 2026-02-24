#include<stdio.h>
#include<string.h>

int main()
{
    char str1[50], str2[50];
    printf("Enter a Sentence: ");
    fgets(str1, sizeof(str1), stdin);
    int i = 0;
    while (str1[i] != '\n' && str1[i] != '\0') {
        i++;
    }
    str1[i] = '\0';
    for (int j = i-1; j>=0; j--) {
        str2[i-j-1] = str1[j];
    }
    for (int l = 0; l<i; l++) {
        printf("%c", str2[l]);
    }
    return 0;
}