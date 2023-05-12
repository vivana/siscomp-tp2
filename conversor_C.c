#include <stdio.h>
#include <stdlib.h>


///∗ prototipo para la rutina en ensamblador ∗/
extern double convert_asm(float, float) __attribute__((cdecl));

double convertir_asm (float base, float tasa){
    double ret_conversion;
    //ret_conversion = asm_main();
    ret_conversion = convert_asm(base, tasa);
   
    return ret_conversion;
    //return tasa;
}

int main(void){
convertir_asm(5,2);  
}
