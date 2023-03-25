function matrixReshape(mat, r, c) {
  const m = mat.length;
  const n = mat[0].length;
  if (m * n !== r * c) {
    return mat;
  }

  // Create the new reshaped matrix
  const newMat = Array.from({ length: r }, () => new Array(c).fill(0));
  let row = 0;
  let col = 0;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      newMat[row][col] = mat[i][j];
      col++;
      if (col === c) {
        col = 0;
        row++;
      }
    }
  }
  return newMat;
}
