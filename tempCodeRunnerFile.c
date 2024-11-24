#include <stdio.h>
int main()
{
    int debut,fin;
    printf("donner le debut:\n");
    scanf("%d",&debut);
    printf("donner le fin:\n");
    scanf("%d",&fin);
    printf("Somme des entiers pairs entre %d to %d = %d\n", debut,
fin,bla(debut, fin));
}
int bla(int x,int y)
{
    if (x>y) 
     return 0;
    else if (x/2==0)
    {
        return(x+bla(x+2,y));
    }

}