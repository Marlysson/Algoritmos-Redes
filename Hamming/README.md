# Implementation of Hamming Algorithm

## API OF FRAME

> **Note :** Operation in a instance of FRAME

```python
frame = Frame(bit_values)
```

### IS_VALID()

> Check whether bits of frame has values not accepted.

**Signature:** ```frame.is_valid()```

**Return:** ```boolean```

**Usage:**

```python
>>> Frame("0101").is_valid()
True
>>> Frame("1234").is_valid()
False
```

### CHANGE_BIT(position)

> Change value of a bit position of a frame

**Signature:** ```frame.change_bit(position)```

**Return:** ```Frame()``` ( _A new frame object with position value changed_ )

**Usage:**

```python
>>> f = Frame("0111")
>>> print(f)
<Frame [0111]>
>>> f.change_bit(1)
<Frame [1111]>
```

## API METHODS OF HAMMING ALGORITHM

> **Note:** Each operations will be made in a instance of a HAMMING ALGORITHM

```python
hamming = Hamming("parity") # pair or odd
```

### ENCODE(frame)

> Put inside of frame the verification bit, calculating the parity value to each position.

**Signature:** ```hamming.encode(frame)```

**Return:** ```Frame()``` ( _A new frame object with position value changed_ )

**Usage:**

```python
>>> hamming = Hamming("pair")
>>> frame = Frame("010")
>>> frame_encoded = hamming.encode(frame)
>>> print(frame_encoded)
<Frame [100110]>
```

### CHECK(frame)

> Verify whether frame it's correct.

**Signature:** ```hamming.check(frame)```

**Return:** ```boolean```

**Usage:**

```python
>>> frame = Frame("110011")
>>> hamming.check(frame)
True
```

## UTILITIES IN API HAMMING

> This methods are also ran on a instance of **hamming algoritm**

### IS_POWER(num,power)

> Return whether a number it's power of other.

**Signature:** ```hamming.is_power(number,power)```

**Return:** ```boolean```

**Usage:**

```python
>>> hamming = Hamming("pair")
>>> hamming.is_power(16, 2)
True
>>> hamming.is_power(24, 4)
False
```

### CALCULATE_PARITY(dataset)

> Return a parity of a dataset , returning a value that means it's a patiry of all values of dataset.

**Signature:** ```hamming.calculate_parity(dataset)```

**Return:** ```integer```

**Usage:**

```python
>>> hamming = Hamming("pair")
>>> hamming.calculate_parity([0,0,0,1])
1
>>> hamming.calculate_parity([1, 1, 0, 0])
0
```

### DIVISORS(value)

> Return all divisors of parameter that are power of two.

> **Note:** The parameter isn't a power of two.

```python
>>> hamming = Hamming("odd")
>>> hamming.divisors(7)
[4, 2, 1]
>>> hamming.divisors(10)
[8, 2]
```

### BITS_VERIFIED_BY(sequence, power_two)

> Return one dataset of values (0's or 1's) of the sequence passed by parameter. This sequence it's the position which don't are power of two and which the second parameter ( power_two ) verify ( turn parity bit of result dataset of bits ); the verifiers bits by them.

```python
>>> hamming = Hamming("odd")
>>> hamming.bits_verified_by(1, 0, 1, 1, 0, 0) , 1 )
[1, 0]
>>> hamming.bits_verified_by([1, 1, 0, 0, 1, 1] , 2 )
[0, 1]
```

## That's all folks. :smile: :+1:
Any sugestions, issues and pull request will be well accepted.