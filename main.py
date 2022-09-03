def on_b_pressed():
    statusbar.value += 5
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

statusbar: StatusBarSprite = None
_type = 0
statusbar = statusbars.create(50, 4, StatusBarKind.health)
statusbar.position_direction(CollisionDirection.TOP)
statusbar.value = 0
scene.set_background_color(11)
mySprite = sprites.create(img("""
        . . . . . . 1 1 1 1 . . . . . . 
            . . . . . 1 1 1 1 1 1 . . . . . 
            . . . . 1 1 9 1 1 1 1 1 . . . . 
            . . . 1 1 9 1 1 1 1 1 1 1 . . . 
            . . . 1 9 1 1 1 1 1 1 1 1 . . . 
            . . . 1 1 1 1 1 1 1 1 1 1 . . . 
            . . . 1 1 1 1 1 1 1 1 1 1 . . . 
            . . . 1 1 1 1 1 1 1 1 1 1 . . . 
            . . . 1 1 1 1 1 1 1 1 1 1 . . . 
            . . . 1 1 1 1 1 1 1 1 1 1 . . . 
            . . . 1 1 1 1 1 1 1 1 1 1 . . . 
            . . . 1 1 1 1 1 1 1 1 1 1 . . . 
            . . . 1 1 1 1 1 1 1 1 1 1 . . . 
            . . . 1 1 1 1 1 1 1 9 1 1 . . . 
            . . . 1 1 1 1 1 1 9 1 1 1 . . . 
            . . . . 1 1 1 1 1 1 1 1 . . . .
    """),
    SpriteKind.player)
mySprite.scale = 5

def on_forever():
    global _type
    if statusbar.value == 100:
        statusbar.value = 0
        _type = 1
    if _type == 1:
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . 7 7 7 7 7 7 7 7 7 . . . . 
                        . . 7 7 7 7 7 7 7 7 7 7 7 . . . 
                        . . 7 7 7 1 1 1 1 1 7 7 7 . . . 
                        . . 7 7 7 1 1 f 1 1 7 7 7 7 . . 
                        . 7 7 7 7 1 1 f 1 1 7 7 7 7 7 . 
                        7 7 7 7 7 1 1 1 1 1 7 7 7 7 7 7 
                        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
        """))
forever(on_forever)
