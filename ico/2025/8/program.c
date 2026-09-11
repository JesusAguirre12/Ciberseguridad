#include <stdio.h>  
#include <string.h>  

int main() {  
    char buffer[10];  
    printf("Enter a string: ");  
    gets(buffer);  
    printf("You entered: %s\n", buffer);  
    return 0;  
}
