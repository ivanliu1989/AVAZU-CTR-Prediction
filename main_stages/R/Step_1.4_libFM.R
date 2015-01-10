### libSVM ###
library(SparseM); require(e1071)  
X2 <- as.matrix.csr(X)

i <- c(1,3:8)
j <- c(2,9,6:10)
x <- 7 * (1:7)
X <- sparseMatrix(i, j, x = x)

X.csc <- new("matrix.csc", ra = X@x,
             ja = X@i + 1L,
             ia = X@p + 1L,
             dimension = X@Dim)
X.csr <- as.matrix.csr(one_hot_1)
range(as.matrix(X) - as.matrix(X.csc))
write.matrix.csr(X.csr, y=train_id_click[2], file='data/libSVM_file.dat')
