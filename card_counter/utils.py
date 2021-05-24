



hx = "#FeeFFF"
def main(screen,t):
    lst = [diamond,heart,spade,club]
    for i in range(-360,640,250):
        t.up()
        t.goto(i,t.ycor())
        t.down()
        a = lst.pop()
        a(t,100,"red")

def diamond(t,d,color):
    d = d*1.4
    t.color(color)
    t.begin_fill()
    t.seth(65)
    t.fd(d)
    t.lt(65)
    t.fd(d)
    t.lt(100)
    t.fd(d)
    t.lt(65)
    t.fd(d)
    t.end_fill()

def heart(t,d,color):
    d = d*1.4
    t.goto(t.xcor(),t.ycor() - (d*.5))
    t.color(color)
    t.begin_fill()
    t.seth(40)
    t.fd(d)
    t.circle(d/2,200)
    t.seth(120)
    t.circle(d/2,200)
    t.fd(d)
    t.end_fill()

def spade(t,d,color):
    t.color(color)
    t.seth(90)
    f = t.pos()
    t.circle(d/2,-200)
    s,sh = t.pos(),t.heading()
    t.circle(d/2,200)
    t.begin_fill()
    t.circle(-d/2,-200)
    t.goto(f[0],f[1]+d+d*.25)
    t.goto(s)
    t.seth(sh)
    t.circle(d/2,200)
    t.end_fill()
    stem = d*.25
    t.begin_fill()
    t.goto(t.xcor()-stem/2,t.ycor())
    t.goto(t.xcor(),t.ycor()-d*3/4)
    t.goto(t.xcor()+stem,t.ycor())
    t.goto(t.xcor(),t.ycor()+d*3/4)
    t.end_fill()

def club(t,d,color):
    t.color(color)
    t.seth(90)
    t.begin_fill()
    t.circle(-d/2,-300)
    t.circle(d/2,300)
    t.circle(-d/2,-300)
    t.end_fill()
    stem = d*.25
    t.begin_fill()
    t.goto(t.xcor()-stem/2,t.ycor())
    t.goto(t.xcor(),t.ycor()-d*3/4)
    t.goto(t.xcor()+stem,t.ycor())
    t.goto(t.xcor(),t.ycor()+d*3/4)
    t.end_fill()

def reset(t):
    t.home()
    t.clear()
    return
