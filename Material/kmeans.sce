//gera dados
x = rand(100,2,'normal');
x = [x; rand(100,2,'normal')+10];
x = [x; rand(100,2,'normal')+2];
plot(x(:,1),x(:,2),'.')

K = 3;

//s = dimensões de x (linhas e colunas)
s = size(x);

pvelho = ones(s(1),1);

// centros aleatórios
c = rand(K,s(2));

while 1
// cálculo das distâncias de todos os X para todos os C
for k = 1:K
    d = (x-ones(s(1),1)*c(k,:)).^2;
    d = sum(d,2);
    D(:,k) = sqrt(d);
end

// encontra os C mais próximos de cada X
[m,p] = min(D,'c');

// verifica se mudou os rótulos
if sum(pvelho == p)==s(1)
    break;
end
pvelho = p;

// atualiza (desloca) os centros
for k = 1:K
    c(k,:) = sum(x(p==k,:),1)/sum(p==k);
end
end

plot(x(p==1,1), x(p==1,2),'r.')
plot(x(p==2,1), x(p==2,2),'g.')
plot(x(p==3,1), x(p==3,2),'b.')
plot(c(:,1),c(:,2),'k*')
