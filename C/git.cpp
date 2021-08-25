#include<cstdio>

int main()
{
    printf("1. git init\n");
    printf("2. git config -g user.name \"\"\n");
    printf("3. git config -g user.email \"\"\n");
    printf("4. git remote add origin URL\n");
    printf("\nAdding\n");
    printf("1. git add -A\n");
    printf("2. git commit -m \"text\"\n");
    printf("3. git push -u origin branch\n");
    printf("\nDownloading\n");
    printf("git clone URL\n");
    printf("\nETC\n");
    printf("git branch\ngit checkout\ngit reset commitnum --hard\n git revert commitnum\n");
    return 0;
}