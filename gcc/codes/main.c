#include<avr/io.h>
#include<stdbool.h>
int main(){

bool p,q,r,s, f;

DDRD = 0b00000000;
DDRB |= (1<<DDB5);

while(1)
   {
	   p = (PIND & (1<<PIND2)) == (1<<PIND2);	
	   q = (PIND & (1<<PIND3)) == (1<<PIND3);
	   r = (PIND & (1<<PIND4)) == (1<<PIND4);
	   s = (PIND & (1<<PIND5)) == (1<<PIND5);

	f = ((!p)&&(!q)) || ((!p)&&(s)) || (r&&(!s)) || (q&&r);
	
	PORTB = (f<<PB5);

   }


}

