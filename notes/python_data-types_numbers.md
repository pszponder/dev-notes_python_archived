# Numbers in Python

```python
# Integers
x0 = -10
x1 = 0
x2 = 10

# Floating-Point Numbers
y0 = -3.14
y1 = 0
y2 = 3.14
```

## Math Operators

From _highest_ to _lowest_ precedence
| Operators | Operation | Example |
|-----------|--------------------------|-----------------|
| `()` | Parenthesis | `(20 - 3) = 17`|
| `**` | Exponent | `2 ** 3 = 8` |
| `%` | Modulus / Remainder | `22 & 8 = 6` |
| `//` | Integer / Floor Division | `22 // 8 = 2` |
| `/` | Division | `22 / 8 = 2.75` |
| `*` | Multiplication | `3 * 3 = 9` |
| `-` | Subtraction | `5 - 2 = 3` |
| `+` | Addition | `2 + 2 = 4` |

Examples of expressions

```python
>>> 2 + 3 * 6
# 20

>>> (2 + 3) * 6
# 30

>>> 2 ** 8
#256

>>> 23 // 7
# 3

>>> 23 % 7
# 2

>>> (5 - 1) * ((7 + 1) / (3 - 1))
# 16.0
```

## Augmented Assignment Operators

Assignment operators allow us to take a variable and update its value all on one line. This is actually a shorthand technique.

| Operator   | Equivalent      |
| ---------- | --------------- |
| `var += 1` | `var = var + 1` |
| `var -= 1` | `var = var - 1` |
| `var *= 1` | `var = var * 1` |
| `var /= 1` | `var = var / 1` |
| `var %= 1` | `var = var % 1` |

- `+=` => Add to the current variable value
- `-=` => Subtract from the current variable value
- `*=` => Multiply the current variable value
- `/=` => Divide the current variable value
- `//=` => Divide the current variable and round it down to the nearest integer
- `**=` => Take the exponent of the variable
- `%=` =>

```python
prize_money = 500
prize_money += 75  # 525
prize_money -= 500 # 125
prize_money *= 10  # 1250
prize_money /= 2   # 625
```

## Math functions

### Round a Floating Point Number

Use the `round()` function to round a floating point number to the nearest integer value.

```python
# Round down anything smaller than x.4
round(1.2) # 1
round(1.4) # 1

# Round up anything greater than or equal to x.5
round(1.5) # 2
round(1.7) # 2
```

### Get the Absolute Value

```python
abs(-10) # 10
abs(-20) # 20
abs(20)  # 20
```

## Bitwise Operators

### Bitwise `&` Operator

Bitwise operators are similar to logical operators, but instead of operating on boolean values, they apply the same logic to all the bits in a value.

A `1` in binary is the same as `True`, while `0` is `False`. So really a bitwise operation is just a bunch of logical operations that are completed in tandem.

> [! NOTE] `&` Bitwise Operator
> `&` is the bitwise `AND` operator in Python

#### Example of using Bitwise And

It's common practice in backend development to store user permissions as binary values. Think about it, if I have `4` different permissions a user can have, then I can store that as a 4-digit binary number, and if a certain bit is present, I know the permission is enabled.

Let's pretend we have 4 permissions:

- `can_create_guild` - Leftmost bit
- `can_review_guild` - Second to left bit
- `can_delete_guild` - Second to right bit
- `can_edit_guild` - Rightmost bit

Which are represented by `0b0000`. For example, if a user only has the `can_create_guild` permission, their binary permissions would be `0b1000`. A user with `can_review_guild` and `can_edit_guild` would be `0b0101`.

To check for, say, the `can_review_guild` permission, we can perform a bitwise `AND` operation on the user's permissions and the enabled `can_review_guild` bit (`0b0100`). If the result is `0b0100` again, we know they have that specific permission!

**Assignment:**
Assign a binary value to the `user_permissions` variable so that the user will have the `can_review_guild` permission and the `can_delete_guild` permission.

```python
user_permissions = 0b0110

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

user_can_create_guild = user_permissions & can_create_guild == can_create_guild
user_can_review_guild = user_permissions & can_review_guild == can_review_guild
user_can_delete_guild = user_permissions & can_delete_guild == can_delete_guild
user_can_edit_guild = user_permissions & can_edit_guild == can_edit_guild

print(f"user_can_create_guild: {user_can_create_guild}")
print(f"user_can_review_guild: {user_can_review_guild}")
print(f"user_can_delete_guild: {user_can_delete_guild}")
print(f"user_can_edit_guild: {user_can_edit_guild}")

# ======
# Output
# ======
# user_can_create_guild: False
# user_can_review_guild: True
# user_can_delete_guild: True
# user_can_edit_guild: False
```

#### Example 2: Binary Permissions

You're responsible for the code that manages the posting permissions of a popular blogging software: "BloggerBytes".

**Challenge:**

Use binary logic and the provided variables to calculate the following boolean values:

- can_read_posts
- can_edit_posts
- can_delete_posts
- can_create_posts

```python
user_permissions = 0b1010

read_posts_perm = 0b1000
edit_posts_perm = 0b0100
delete_posts_perm = 0b0010
create_posts_perm = 0b0001

can_read_posts = user_permissions & read_posts_perm == read_posts_perm
can_edit_posts = user_permissions & edit_posts_perm == edit_posts_perm
can_delete_posts = user_permissions & delete_posts_perm == delete_posts_perm
can_create_posts = user_permissions & create_posts_perm == create_posts_perm

print(f"The user can read posts: {can_read_posts}")
print(f"The user can edit posts: {can_edit_posts}")
print(f"The user can delete posts: {can_delete_posts}")
print(f"The user can create posts: {can_create_posts}")

# Output
# The user can read posts: True
# The user can edit posts: False
# The user can delete posts: True
# The user can create posts: False
```

### Bitwise `|` Operator

> [! NOTE] Bitwise `|` Operator
> The bitwise "or" (`|`) operator is similar to the bitwise "and" operator in that it works on binary rather than boolean values.
>
> However, the bitewise "or" operator applies "OR" logic instead of "AND" logic

#### Example of Bitwise Or

A "party" is a team of 2-4 players who are online at the same time and fighting together. A guild is a larger group of players, sometimes 50 or 60, who share a common purpose.

We've been asked to add some more functionality to the "guild permissions" system. When players are in a party, they gain the guild permissions of all the other members of the party!

**Assignment**
Create a new variable:
`party_perms`: A binary number. Use bitwise `OR` operations to get the superset of all the permissions of the members of the party (Glorfindel, Galadriel, Elendil and Elrond)

```python
glorfindel_perms = 0b0001
galadriel_perms = 0b0010
elendil_perms = 0b0001
elrond_perms = 0b1011

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

party_perms = glorfindel_perms | galadriel_perms | elendil_perms | elrond_perms

party_can_create_guild = party_perms & can_create_guild == can_create_guild
party_can_review_guild = party_perms & can_review_guild == can_review_guild
party_can_delete_guild = party_perms & can_delete_guild == can_delete_guild
party_can_edit_guild = party_perms & can_edit_guild == can_edit_guild

print(f"party_perms: 0b{party_perms:b}")
print(f"party_can_create_guild: {party_can_create_guild}")
print(f"party_can_review_guild: {party_can_review_guild}")
print(f"party_can_delete_guild: {party_can_delete_guild}")
print(f"party_can_edit_guild: {party_can_edit_guild}")

# ======
# Output
# ======
# party_perms: 0b1011
# party_can_create_guild: True
# party_can_review_guild: False
# party_can_delete_guild: True
# party_can_edit_guild: True
```
