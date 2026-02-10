# Bank System — Function-Based Design

This module simulates a basic banking system using Python functions.

The objective is to understand how financial operations can be separated into
independent, reusable units of logic.

---

## Operations Implemented

- Check account balance
- Deposit money
- Withdraw money
- Prevent overdraft

---

## Design Approach

Each banking operation is implemented as a **separate function**.
A shared global variable represents account balance to demonstrate
controlled use of global state.

---

## Key Learning

- When and why to use global variables
- How real banking logic is structured
- Clean separation of responsibilities
