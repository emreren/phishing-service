# Phishing Service

Phishing Service, phishing feeds paylaşımı yapan kaynaklardan URL'leri çeken, veritabanına kaydeden ve FastAPI aracılığıyla bu URL'leri sunan bir uygulamadır.

## Başlangıç

Bu talimatlar, projenin yerel makinenizde nasıl çalıştırılacağı veya dağıtılacağı hakkında size rehberlik edecektir. Geliştirme ve test amacıyla bu adımları takip edebilirsiniz.

## Önkoşullar

Projenin çalışması için aşağıdaki yazılımların yüklü olması gerekmektedir:

- Docker
- Docker Compose
- Python 3.11

Ayrıca, .env dosyasında PostgreSQL veritabanı bağlantı bilgilerini ve çekilecek URL listesini ayarladığınızdan emin olun.

## Kurulum

1. Proje klasörüne gidin:

```bash
cd phishing_service
```

2. Docker Compose ile projeyi başlatın:

```bash
docker-compose up -d
```
Bu komut, PostgreSQL veritabanı ve iki farklı container'ı başlatacak; veritabanını oluşturacak, URL'leri çekip veritabanına kaydedecek ve FastAPI sunucusunu başlatacaktır.

3. Proje çalıştıktan sonra API'ye aşağıdaki adres üzerinden erişebilirsiniz:

```bash
http://localhost:8000/phishing-urls/
```

### API Endpointleri

**GET /phishing-urls/:** Veritabanındaki phishing URL'lerini listeleyen bir endpointtir. Sayfalama için **skip** ve **limit** parametrelerini kullanabilirsiniz.

```bash
http://localhost:8000/phishing-urls/?limit=100

http://localhost:8000/phishing-urls/?limit=20&skip=20
```

### Environment Variables

Proje, `.env` dosyasında belirtilen çevresel değişkenleri kullanır. Bu değişkenler, veritabanı bağlantı bilgilerini ve çekilecek URL listesini içerir.

- `POSTGRES_USER`: PostgreSQL veritabanı kullanıcı adı
- `POSTGRES_PASSWORD`: PostgreSQL veritabanı şifresi
- `POSTGRES_HOST`: PostgreSQL veritabanı host adresi
- `POSTGRES_DB`: PostgreSQL veritabanı adı
- `URLS`: Phishing URL'lerini çekmek için kullanılacak URL listesi. Virgülle ayrılmış bir liste olarak girilmelidir.

### Katkıda Bulunma

Katkıda bulunmak için bu depoyu forklayın, değişikliklerinizi yapın ve bir pull isteği gönderin.
