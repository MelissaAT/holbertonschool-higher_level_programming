#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasks = {};

    for (let i = 0; i < todos.length; i++) {
      const todo = todos[i];
      if (todo.completed) {
        const userId = todo.userId;
        if (completedTasks[userId] !== undefined) {
          completedTasks[userId]++;
        } else {
          completedTasks[userId] = 1;
        }
      }
    }

    console.log(completedTasks);
  }
});
