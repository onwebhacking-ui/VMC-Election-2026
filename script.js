fetch('data.json')
  .then(response => response.json())
  .then(data => {
    let output = '';
    data.forEach(user => {
      output += `<p>${user.name} - ${user.age}</p>`;
    });
    document.getElementById('output').innerHTML = output;
  });
