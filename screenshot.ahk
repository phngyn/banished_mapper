;IMPORTANT: 1. change the screenshot (with UI) key to P, the default one somehow
;              doesn't work for me and this script relies on that little detail 
;           2. change resolution to 800x600 windowed! (Should work fullscreen too,
;              but I didn't try)

#InstallMouseHook
#InstallKeyBDHook

SetKeyDelay, 50, 50
SetMouseDelay, 50

seed = 322 ;Starting seed
stopseed = 2000 ;Generate maps untill you hit this 

!y:: ; Press Alt+y to start the script

Loop
{
MouseClick, left,  1700,  550 ;New
MouseClick, left,  1790,  590 ;cursor
MouseClick, left,  1790,  590 ;cursor
Send, {BS 12} ;delete random number
Send, %seed%  ;type seed
Send, {F12}  ;take screenshot of seed;
MouseClick, left,  1950,  920 ;Ok

Sleep 20000 ; 30 secs
; Loop
; {
;     PixelGetColor, color, 1620, 1313 ;check whether loading is done

;     if (color = 0xFEFEFE) ; R254 G254 B254
;     {
;     break
;     }
;     ; Otherwise continue waiting

;     Sleep 100 ; 30 secs
; }
Send, {F2} ;open menu 2
Send, {3}  ;open mini map
Send, {F12}  ;take screenshot
Send, {ESC}
MouseClick, left,  1700,  890 ;quit
Sleep 3000  ;wait a bit till loading the main menu has begun
; Sleep 500  ;wait a bit till loading the main menu has begun
; Loop
; {
;     PixelGetColor, color, 1700,  550 ;checking whether we are in the main menu

;     if (color = 0x45403C) ; R69 G64 B60
;     break

;     ; Otherwise, continue waiting 

;     Sleep 100
; }

seed += 1 ;don't want to generate the same map again...

if (seed > stopseed) 
break ;you don't want to keep running forever

}

Return