'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.


'''
SW=600
SH=600
import arcade
import random
class Flake():
    def __init__(self,pos_x,pos_y,radius,dx,dy,col):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.radius=radius
        self.dx=dx
        self.dy=dy
        self.col=col
    def draw_flake(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.radius,self.col)
        arcade.draw_rectangle_filled(SW/2,SH/2,SW,(SW/SH)*10,arcade.color.FRENCH_BEIGE)
        arcade.draw_rectangle_filled(SW/2,SH/2,(SW/SH)*10,SH,arcade.color.FRENCH_BEIGE)
    def update_flake(self):

        self.pos_x+=self.dx
        self.pos_y+=self.dy
        if self.pos_y==SH-SH:
            self.pos_y=random.randint(0,SH)
        if self.pos_x>=SW or self.pos_x<=0:
            self.pos_y=random.randint(0,SH)
        if self.dx==1 or self.dx==-1:
            self.dy=random.randint(-3,-2)


class MyGame(arcade.Window):
    def __init__(self,SW,SH,title):
        super().__init__(SW,SH,title)
        arcade.set_background_color(arcade.color.BLACK)
        self.flake_list=[]
        for i in range(300):
            radius=random.randint(1,3)
            pos_x=random.randint(0,600)
            pos_y=random.randint(600,700)
            dx=random.randint(-1,1)
            dy=random.randint(-4,-1)
            if i==0:
                col=(arcade.color.RED)
            else:
                col=(arcade.color.WHITE)
            flake=Flake(pos_x,pos_y,radius,dx,dy,col)
            self.flake_list.append(flake)


    def on_draw(self):
        arcade.start_render()
        for flake in self.flake_list:
            flake.draw_flake()

    def on_update(self, dt):
        for flake in self.flake_list:
            flake.update_flake()










def myprogram():
    window=MyGame(SW,SH,"Hermonator 2: Judgement Day")
    arcade.run()
if __name__=="__main__":
    myprogram()




