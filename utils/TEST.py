r = 25
y = 0
e = "-"
q = 0
ee = False

for x in range(36):
    print(
        f'Button(Button_x * {y + 1}, (HEIGHT - TOOLBAR_HEIGHT / 2 {e} {r}), 10, 10, ({int(x * 7.083)}, {int(x * 7.083)}, {int(x * 7.083)})),')
    y += 1
    if q == 1:
        if y == 6:
            y = 0
            r += 10
        if r == 35:
            r = 25
            if ee:
                e = "-"
                ee = False
            else:
                e = "+"
                ee = True
    if q == 0:
        if y == 6:
            y = 0
            r -= 10
        if r == -5:
            r = 5
            q += 1
            if ee:
                e = "-"
                ee = False
            else:
                e = "+"
                ee = True

print()

r = 25
y = 0
e = "-"
q = 0
ee = False

for x in range(30):
    print(
        f'Button(Button_x * {y + 7}, (HEIGHT - TOOLBAR_HEIGHT / 2 {e} {r}), 10, 10, ({int((x+1) * 8.5)},0,0)),')
    y += 1
    if q == 1:
        if y == 5:
            y = 0
            r += 10
        if r == 35:
            r = 25
            if ee:
                e = "-"
                ee = False
            else:
                e = "+"
                ee = True
    if q == 0:
        if y == 5:
            y = 0
            r -= 10
        if r == -5:
            r = 5
            q += 1
            if ee:
                e = "-"
                ee = False
            else:
                e = "+"
                ee = True

print()

r = 25
y = 0
e = "-"
q = 0
ee = False

for x in range(30):
    print(
        f'Button(Button_x * {y + 12}, (HEIGHT - TOOLBAR_HEIGHT / 2 {e} {r}), 10, 10, (0,{int((x+1) * 8.5)},0)),')
    y += 1
    if q == 1:
        if y == 5:
            y = 0
            r += 10
        if r == 35:
            r = 25
            if ee:
                e = "-"
                ee = False
            else:
                e = "+"
                ee = True
    if q == 0:
        if y == 5:
            y = 0
            r -= 10
        if r == -5:
            r = 5
            q += 1
            if ee:
                e = "-"
                ee = False
            else:
                e = "+"
                ee = True

print()

r = 25
y = 0
e = "-"
q = 0
ee = False

for x in range(30):
    print(
        f'Button(Button_x * {y + 17}, (HEIGHT - TOOLBAR_HEIGHT / 2 {e} {r}), 10, 10, (0,0,{int((x+1) * 8.5)})),')
    y += 1
    if q == 1:
        if y == 5:
            y = 0
            r += 10
        if r == 35:
            r = 25
            if ee:
                e = "-"
                ee = False
            else:
                e = "+"
                ee = True
    if q == 0:
        if y == 5:
            y = 0
            r -= 10
        if r == -5:
            r = 5
            q += 1
            if ee:
                e = "-"
                ee = False
            else:
                e = "+"
                ee = True
