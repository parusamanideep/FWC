.include "/usr/share/avra/m328Pdef.inc"

.def P = R26
.def Q = R25
.def R = R18
.def S = R19
.def F = R20
.def temp = R22
.def mask = R23
.def result = R24

ldi R16, 0b00000000
out DDRD, R16
ldi R16, 0b00100000
out DDRB, R16

ldi mask, 0b00000001

start:
in R17, PIND
lsr R17
lsr R17
mov P, R17
and P, mask
lsr R17
mov Q, R17
and Q, mask
lsr R17
mov R, R17
and R, mask
lsr R17
mov S, R17
and S, mask

mov result, P
eor result, mask
mov temp,Q
eor temp, mask
and result, temp

mov temp, P
eor temp, mask
and temp, S
or result, temp

mov temp, S
eor temp, mask
and temp, R
or result, temp

mov temp, Q
and temp, R
or result, temp

lsl result
lsl result
lsl result
lsl result
lsl result
out PORTB, result
