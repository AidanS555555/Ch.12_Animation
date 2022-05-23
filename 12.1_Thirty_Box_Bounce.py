'''
30 BOX BOUNCE PROGRAM
--------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
'''
SW=600
SH=600
rail=10
import random
import arcade

class Ball():
    def __init__(self,pos_x,pos_y,s,dx,dy,c):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.s=s
        self.dx=dx
        self.dy=dy
        self.col=c
    def draw_ball(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.s, self.s, self.col)
    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        if self.pos_x<=rail+self.s/2:
            self.dx *= -1
            self.col=arcade.color.BOTTLE_GREEN
        if self.pos_x>=SW-rail-self.s/2:
            self.col=arcade.color.ORIOLES_ORANGE
            self.dx *= -1
        if self.pos_y<=rail+self.s/2:
            self.col=arcade.color.DARK_BROWN
            self.dy *= -1
        if self.pos_y>=SH-rail-self.s/2:
            self.col=arcade.color.PURPLE_MOUNTAIN_MAJESTY
            self.dy *= -1






class MyGame(arcade.Window):
    def __init__(self,SW,SH,title):
        super().__init__(SW,SH,title)
        arcade.set_background_color(arcade.color.GRAY)
        self.ball_list=[]
        for i in range(30):
            s = random.randint(2,75)
            x = random.randint(s,SW-s)
            y = random.randint(s,SH-s)
            dx = random.randint(-3,3)
            dy = random.randint(-3, 3)
            c =(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            ball = Ball(x,y,s,dx,dy,c)
            if dx==0:
                dx+=4
            self.ball_list.append(ball)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(rail/2,SH/2,rail,SH,arcade.color.BOTTLE_GREEN)
        arcade.draw_rectangle_filled(SW/2, SH-rail/2, SW, rail, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
        arcade.draw_rectangle_filled(SW-rail/2, SH / 2, rail, SH, arcade.color.ORIOLES_ORANGE)
        arcade.draw_rectangle_filled(SW/2, rail/2, SW, rail, arcade.color.DARK_BROWN)
        for ball in self.ball_list:
            ball.draw_ball()
    def on_update(self, dt):
        for ball in self.ball_list:
            ball.update_ball()
def myprogram():
    window=MyGame(SW,SH,"The Hermonator")
    arcade.run()

if __name__=="__main__":
    myprogram()