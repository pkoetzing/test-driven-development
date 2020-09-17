# [Unit Testing in Python — The Basics](https://medium.com/swlh/unit-testing-in-python-basics-21a9a57418a0)

## Why do we test at all

- Trust: You checked at least some cases if they work. So others can have more
trust in the quality of your work and you can also put more trust in it.

- Breaking Changes: For a bigger project, it is sometimes hard to have every
part in mind. By writing tests, you make it easier to change something and see
if / where things break. This does not only help you but also team members.
Including once that are not there yet.

- Code Style: When you know that you have to write tests, you write some things
slightly differently. Those slight differences usually improve the coding
style. Sometimes, they are crucial. For example, if you have to thoroughly test
your code you will make smaller chunks.

- Documentation: Some test cases show a little bit of how the code is intended
to be used.

## Test Coverage

I hope at this point we agree that having tests is a good idea. But how many
tests do you need? When did you test everything?
A group of measures for this is the test coverage. There are two relevant types
of test coverage: Line coverage and branch coverage.

## Good Tests

It’s pretty hard to write good tests and when you measure your test coverage
it is tempting to quickly write a couple of bad tests.

- Worst is no testing at all.
- A little bit better is a test that just executes a function but does not
check if the return value/the side effects are what you expect. So you simply
run it to check if the code crashes.
- Happy-Tests where you check the output of the tested function and a typical
input is even better. I call them happy because they test what you expect to
get.
- In contrast, an unhappy execution path is dealing with unwanted inputs. This
is also called negative testing. You check if you actually throw an error. Not
throwing an error and silently failing is bad as it hides bugs.
- Property testing is pretty cool. There you don’t test for single values, but
you check if a property is still held. For example, the output of a
factorization function can be multiplied and should equal the input.
