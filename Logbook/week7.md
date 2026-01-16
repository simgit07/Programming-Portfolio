## Summary

This lecture introduces **Sets** and **Dictionaries**, two powerful Python collection types that are used when lists and tuples aren’t the best fit.

**Sets** are collections of **unique values** with no guaranteed order. They are great when **we** care about **membership** (whether something is present), **removing duplicates**, or performing **mathematical set operations** like union and intersection. Because sets don’t have positions, **we** can’t index or slice them—but **we** *can* efficiently test membership and combine them with other sets.

Sets can be **mutable** (normal `set`) or **immutable** (`frozenset`). Python supports set comprehensions, making it easy for **us** to build sets programmatically.

**Dictionaries** store data as **key–value pairs**, allowing fast lookup of values using unique keys. They’re ideal for representing structured data like records, configurations, or mappings (e.g., product → price). Dictionaries are mutable and, in modern Python, **preserve insertion order**.

In this lecture, **we** learn multiple ways to create dictionaries, how to loop through keys, values, or items, and how dictionaries work with functions using `**kwargs` for flexible keyword arguments.

The lecture ends by comparing **Lists, Tuples, Sets, and Dictionaries**, helping **us** choose the right data structure depending on mutability, ordering, uniqueness, and lookup needs.

---

## Key Technologies 

### Sets

* **Set characteristics**

  * Unordered
  * No duplicates
  * Elements must be immutable
* **Creating sets**

  * `{1, 2, 3}`
  * `set(iterable)`
  * Set comprehensions `{x for x in ...}`
* **Set operations**

  * Union (`|`)
  * Intersection (`&`)
  * Difference (`-`)
  * Symmetric difference (`^`)
* **Subset / superset checks**

  * `<`, `<=`, `>`, `>=`
* **Mutable vs immutable**

  * `set` vs `frozenset`
* **Common methods**

  * `add()`, `remove()`, `pop()`, `update()`

---

### Dictionaries

* **Key–value pairs**
* **Keys**

  * Must be unique
  * Must be immutable
* **Values**

  * Can be any type
  * Can repeat
* **Creating dictionaries**

  * `{key: value}`
  * `dict()`
  * Dictionary comprehensions `{k: v for ...}`
* **Access & modification**

  * `dict[key]`
  * `del dict[key]`
  * `in` keyword for key checking
* **Important methods**

  * `keys()`, `values()`, `items()`
  * `get()`, `update()`, `pop()`
* **Iteration**

  * Over keys, values, or key–value pairs
* **Functions & dictionaries**

  * `**kwargs` (packing)
  * `**dict` (unpacking)


### Choosing the Right Collection

* **List** → ordered, mutable, duplicates allowed
* **Tuple** → ordered, immutable, mixed types
* **Set** → unordered, unique values, fast membership tests
* **Dictionary** → fast lookup using keys, structured data

-