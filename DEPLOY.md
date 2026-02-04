# Guia de Deploy e Rollback

## Como fazer deploy

1. Construa e teste localmente:
```bash
docker build -t sre-app:1.0.1 app/
docker run -p 8080:8080 sre-app:1.0.1
```

2. Execute os testes:
```bash
cd tests && pytest -v
```

3. Execute o deploy:
```bash
./deploy.sh 1.0.1
```

4. Monitore a aplicação:
```bash
./monitor.sh
```

---

## Como fazer rollback

Se algo der errado após o deploy:

1. Execute o rollback:
```bash
./rollback.sh
```

2. Verifique se a versão anterior voltou:
```bash
curl http://localhost:8080/health
```

3. Investigue o problema antes de tentar novo deploy

---

## Checklist de Deploy

- Testes passando localmente  
- Pipeline do GitHub passou  
- Versão anterior está taggeada  
- Notificou a equipe  
- Monitore por 15 minutos após deploy  

---

## Comandos rápidos de teste

```bash
# Torne os scripts executáveis
chmod +x deploy.sh rollback.sh

# Faça um deploy
./deploy.sh 1.0.0

# Verifique se está funcionando
./monitor.sh

# Simule um rollback
./rollback.sh

# Verifique se voltou
./monitor.sh
```

---

## Validação

- Script de deploy executa sem erros  
- Script de rollback restaura versão anterior  
- Documentação está clara e pode ser seguida por outra pessoa  
- Health checks funcionam após deploy e rollback  

