CREATE TABLE news (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    info TEXT NOT NULL,
    author VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TYPE content_type AS ENUM ('novel', 'video');

CREATE TABLE content (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    type content_type NOT NULL,
    url TEXT NOT NULL 
);

-- Inserindo dados fictícios para a tabela news
INSERT INTO news (title, info, author) VALUES 
('Lançamento do novo sistema de streaming da Globo', 'A Globo anuncia hoje seu novo serviço de streaming com conteúdo exclusivo e produções internacionais.', 'Carlos Drummond'),
('Novela "Mar de Paixões" bate recorde de audiência', 'Com mais de 35 pontos no IBOPE, a novela das nove se torna líder absoluta de audiência em 2025.', 'Ana Beatriz Silva'),
('Globoplay expande catálogo com produções independentes', 'Novos filmes e séries de produtores independentes chegam à plataforma este mês.', 'Rafael Oliveira'),
('Estreia de reality show causa polêmica nas redes sociais', 'O novo reality show "Desafio Extremo" dividiu opiniões entre os espectadores logo em seu primeiro episódio.', 'Mariana Costa'),
('Grande Final do BBB 2025 tem recorde de votação', 'Mais de 500 milhões de votos foram computados para decidir o vencedor da 25ª edição do reality.', 'Pedro Almeida'),
('Novo documentário sobre meio ambiente recebe prêmio internacional', 'Produção da Globo sobre Amazônia é reconhecida no Festival de Documentários de Berlim.', 'Juliana Santos'),
('Mudanças na programação matinal da TV Globo', 'Nova atração substituirá programa tradicional nas manhãs a partir de setembro.', 'Felipe Mendes'),
('Série brasileira é indicada ao Emmy Internacional', '"Fronteiras Invisíveis" concorre em três categorias no prêmio mais importante da televisão mundial.', 'Luciana Ferreira');

-- Inserindo dados fictícios para a tabela content
INSERT INTO content (name, description, type, url) VALUES 
('Verdades Secretas III', 'Terceira temporada da aclamada série sobre o mundo da moda e suas obscuridades', 'novel', 'https://globoplay.com/verdades-secretas-3'),
('Avenida Brasil - Edição Especial', 'Reedição da novela com cenas inéditas e comentários do diretor', 'novel', 'https://globoplay.com/avenida-brasil-especial'),
('Documentário: Amazônia - O Último Refúgio', 'Documentário premiado sobre a maior floresta tropical do mundo', 'video', 'https://globoplay.com/amazonia-ultimo-refugio'),
('Master Chef Brasil - Temporada 10', 'Décima temporada do reality show de culinária mais famoso do país', 'video', 'https://globoplay.com/masterchef-10'),
('O Tempo Não Para - Série Completa', 'Todos os episódios da novela sobre viajantes do tempo', 'novel', 'https://globoplay.com/o-tempo-nao-para'),
('Jornal Nacional - Retrospectiva 2024', 'Compilação dos principais acontecimentos noticiados no ano anterior', 'video', 'https://globoplay.com/jn-retrospectiva-2024'),
('Nas Garras da Patrulha', 'Reality show que acompanha o dia a dia de policiais em diversas cidades brasileiras', 'video', 'https://globoplay.com/nas-garras-da-patrulha'),
('Amor de Mãe - Coleção Completa', 'Todos os capítulos da premiada novela sobre maternidade e suas complexidades', 'novel', 'https://globoplay.com/amor-de-mae-completa'),
('The Voice Brasil - Melhores Apresentações', 'Compilação das apresentações mais marcantes do programa musical', 'video', 'https://globoplay.com/the-voice-melhores'),
('Pantanal 2025', 'Remake da clássica novela ambientada no coração do Brasil', 'novel', 'https://globoplay.com/pantanal-2025'),
('Sob Pressão - Nova Temporada', 'Série médica que retrata os desafios da saúde pública no Brasil', 'novel', 'https://globoplay.com/sob-pressao-nova'),
('Pequenas Empresas, Grandes Negócios - Especial Startups', 'Documentário sobre o ecossistema de startups brasileiro', 'video', 'https://globoplay.com/pegn-startups');

