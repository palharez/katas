function alphabetPosition(text) {
  const response = [];
  
  for (const char of text) {
    
    let code = char.toLowerCase().charCodeAt(0) - 96;
    let isLetter = (code > 0 && code < 27);
    
    if(!isLetter) continue;
  
    response.push(code);
  }

  return response.join(' ');
}
