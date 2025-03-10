# Knowledge Base
## Compound Statements

In prolog, **atoms** do not inherently hold meaning. Instead we assign meaning to the different statements that suit our own needs, so comments are essential to understanding.

```prolog
captialCity(paris) /* paris is a capital city */
```

On its own, that statement could be anything, but through the comment we make clear that the purpose of this **compound statement** is that any entry to *captialCity* is a city which is a capital of some country.

```prolog
cityInCountry(paris, france) /* paris is a city in france */
```

The above statement is an entry which gives a city and the country it resides in. These are attributes together which describe something, but it only becomes clear what is being described through the comment. Otherwise perhaps it could be describing that france has a city called paris.

>cityInCountry(paris, Country)

The above statement is a query, because anything that starts with a captial letter is a variable. This statement will look through the knowledge base and find all matches with the known terms, so an entry in **cityInCountry** which has paris as the first value. 

Then it will output all the unknowns, which are assigned as the variable. Therefore if we queried to the preceeding tablebase, it would return france.

```prolog
ingredient(tagine, aubergine, 250). /* tagine congtains 250g of aubergine */
ingredient(tagine, tomato, 100).
```

>ingredient(tagine, Ingredient, Weight)

The above will return all the entries for tagine, but only the **ingredients** and the amount of the ingredients we want. This is because we specified those as variables or in other words the unknowns.

## Rules

Rules can be used to filter through a give knowledge base to find certain applications which match our requirements. This follows the basic format of

> atom :- queryA, queryB.

Note that **,** in prolog means AND, **;** means OR, and **\\** means NOT. Let's look at an example of this in action.

```prolog
parent(fred, jack). /* fred is the father of jack */
parent(fred, alia).
parent(fred, paul).
parent(dave, fred).

grandParent(Grandparent, Child) :- parent(Grandparent, Parent), parent(Parent, Child).

sibling(ChildA, ChildB) :- parent(Parent, ChildA), parent(Parent, ChildB).
```

Firstly, we create a knowledge base of parents and their children and make 4 entries. Then we create a rule called **grandParent**, which takes a **GrandParent** and their **Child**.

This rule basically checks that a given **GrandParent** is the parent of a **Parent**, and that **Parent** is the parent of a **Child**. If both are satisfied, then it will say that it is a true statement.

>grandParent(dave, jack)

Or finding all the grandchildren

>grandParent(dave, GrandChildren)