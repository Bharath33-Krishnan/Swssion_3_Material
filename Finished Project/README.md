# GDUSession3

## Python VS C

> for loops

```python
# python

# range based loop
for i in range(first, last + 1):
    print(i)

# iteratory loop
nums = [1, 4, 6, 2, 3]
for num in nums:
    print(num)
```

```c
// C
for (int i = first; i < last; i++) {
    printf("%d\n", i);
}
```

> while loops

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

```c
int i = 0;

while (i < 10) {
    i++;
    printf("%d\n", i);
}
```

> Pygame vector methods

```python
vec = pygame.Vector2(x, y)

vec.magnitude()
vec.normalize()
vec.angle_to(another_vec)
```

> Pygame rect

```python
rect = pygame.Rect(x, y, width, height)

rect.x # int
rect.y # int
rect.center # [int, int]
rect.centerx # int
rect.centery # int

rect.colliderect(another_rect) # bool
rect.collidepoint(x, y) # bool
```
