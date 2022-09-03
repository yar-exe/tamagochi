controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    statusbar.value += 5
})
let _type = 0
let statusbar: StatusBarSprite = null
statusbar = statusbars.create(50, 4, StatusBarKind.Health)
statusbar.positionDirection(CollisionDirection.Top)
statusbar.value = 0
scene.setBackgroundColor(11)
let mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.scale = 3
forever(function () {
    if (statusbar.value == 100) {
        statusbar.value = 0
        _type = 1
        mySprite.scale += 0.1
    }
    if (_type == 1) {
        mySprite.setImage(img`
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
            `)
    }
})
