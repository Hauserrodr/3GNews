function populateGallery(data) {
    const container = document.querySelector(".gallery-item");

    data.forEach(item => {
        const userContainer = document.createElement('div');
        userContainer.className = 'user-container';

        item.images.forEach(imgSrc => {
            const img = document.createElement('img');
            img.src = imgSrc;
            userContainer.appendChild(img);
        });

        container.appendChild(userContainer);
    });
}

// Your data
const data = [
    {
        "day_str": "http://54.197.18.85:7777/get_all_user_news",
        "headline": "http://54.197.18.85:7777/get_all_user_news",
        "region": "http://54.197.18.85:7777/get_all_user_news",
        "news": "http://54.197.18.85:7777/get_all_user_news",
        "image_prompt": "http://54.197.18.85:7777/get_all_user_news",
        "images": ["http://54.197.18.85:7777/get_all_user_news"],
        "thumbnails": ["http://54.197.18.85:7777/get_all_user_news"]
    },
    {
        "day_str": "http://54.197.18.85:7777/get_all_user_news",
        "headline": "http://54.197.18.85:7777/get_all_user_news",
        "region": "http://54.197.18.85:7777/get_all_user_news",
        "news": "http://54.197.18.85:7777/get_all_user_news",
        "news_source": "[1]: https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/ \"\"\n[2]: https://g1.globo.com/rs/rio-grande-do-sul/noticia/2023/08/27/policia-investiga-suspeita-de-golpe-em-prefeituras-do-rs-apos-furto-de-mais-de-r-1-milhao-em-contas-bancarias.ghtml \"\"\n[3]: https://noticias.uol.com.br/rio-grande-do-sul/noticias/ \"\"\n[4]: https://gauchazh.clicrbs.com.br/ultimas-noticias/tag/rio-grande-do-sul/ \"\"\n[5]: https://agoranors.com/tempo/ \"\"\n\n[As inscrições para o Vestibular 2024 da UFRGS estão abertas até as 23h59 do dia 25 de setembro. A universidade oferece 4.023 vagas de ingresso nos cursos de graduação](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Rio Grande do Sul teve uma manhã com geada e temperaturas negativas, Bom Jesus registrou -4°C. De acordo com a Climatempo, a condição climática deve se estender até terça (29)](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Um jovem foi executado com um tiro durante uma festa rave em Estância Velha, a polícia está investigando a motivação para o assassinato](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[A presidência da Câmara de Porto Alegre vai propor 'revogaço' de lei que tornou 8 de janeiro o 'Dia do Patriota'](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[A Polícia Civil está investigando uma suspeita de golpe contra quatro prefeituras do Rio Grande do Sul. Segundo as investigações, os municípios perderam, ao todo, quase R$1,5 milhão durante ataques eletrônicos nas últimas semanas](https://g1.globo.com/rs/rio-grande-do-sul/noticia/2023/08/27/policia-investiga-suspeita-de-golpe-em-prefeituras-do-rs-apos-furto-de-mais-de-r-1-milhao-em-contas-bancarias.ghtml).\n[Um carro não parou e caiu em um rio, uma mulher morreu no Rio Grande do Sul](https://noticias.uol.com.br/rio-grande-do-sul/noticias/).\n[Rastro de fogo de lixo espacial foi registrado em cidades do RS](https://noticias.uol.com.br/rio-grande-do-sul/noticias/).\n[É impressionante a queda no número de novos registros de armas de fogo no RS](https://gauchazh.clicrbs.com.br/ultimas-noticias/tag/rio-grande-do-sul/).\n[Nuvens carregadas estão provocando temporais isolados pelo Rio Grande do Sul. Segundo a previsão do tempo, o avanço de uma massa de ar frio provoca o declínio nas temperaturas](https://agoranors.com/tempo/).",
        "image_prompt": "http://54.197.18.85:7777/get_all_user_news",
        "images": ["http://54.197.18.85:7777/get_all_user_news"],
        "thumbnails": ["http://54.197.18.85:7777/get_all_user_news"]
    },
    {
        "day_str": "29/08/2023",
        "headline": "\"Rio Grande do Sul: Vestibular, geada, crime, política e fenômeno no céu marcam a semana\"",
        "region": "Viamão",
        "news": "[Universidade Federal do Rio Grande do Sul (UFRGS) abre inscrições para o Vestibular 2024 até as 23h59 do dia 25 de setembro, oferecendo 4.023 vagas de ingresso nos cursos de graduação](^1^).\n[Rio Grande do Sul tem manhã com geada e temperaturas negativas; Bom Jesus registrou -4°C. De acordo com a Climatempo, condição climática deve se estender até terça (29)](^1^).\n[Jovem é executado com tiro durante festa rave em Estância Velha, diz polícia. Corpo foi localizado às margens de uma rodovia em Dois Irmãos, a 16 km do local do crime. Polícia Civil investiga a motivação para o assassinato](^1^).\n[Presidência da Câmara de Porto Alegre vai propor 'revogaço' de lei que tornou 8 de janeiro o 'Dia do Patriota'. De acordo com o Legislativo, entendimento pelo 'revogaço' se deu a partir da repercussão que o tema teve nos últimos dias. Data é a mesma em que ocorreram atos antidemocráticos em Brasília](^1^).\n[Preso suspeito de sequestrar motorista filmado pedindo socorro de dentro do porta-malas de carro em Porto Alegre. Crime aconteceu em maio deste ano. Motorista de aplicativo foi sequestrado após corrida até Viamão, na Região Metropolitana](^1^).\n[Passagem de meteoro deixa rastro de luz no céu sobre Mostardas. Fenômeno foi registrado na noite de domingo (27). \"Fireball\", como são chamados, recebem esse nome por serem como \"bolas de fogo\": com brilho forte e serem fragmentos de um cometa ou asteroide maior](^1^).",
        "news_source": "[1]: https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/ \"\"\n[2]: https://g1.globo.com/rs/rio-grande-do-sul/ \"\"\n[3]: https://noticias.uol.com.br/rio-grande-do-sul/noticias/ \"\"\n[4]: https://gauchazh.clicrbs.com.br/ultimas-noticias/tag/rio-grande-do-sul/ \"\"\n[5]: https://www.cnnbrasil.com.br/tudo-sobre/rio-grande-do-sul/ \"\"\n\n[Universidade Federal do Rio Grande do Sul (UFRGS) abre inscrições para o Vestibular 2024 até as 23h59 do dia 25 de setembro, oferecendo 4.023 vagas de ingresso nos cursos de graduação](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Rio Grande do Sul tem manhã com geada e temperaturas negativas; Bom Jesus registrou -4°C. De acordo com a Climatempo, condição climática deve se estender até terça (29)](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Jovem é executado com tiro durante festa rave em Estância Velha, diz polícia. Corpo foi localizado às margens de uma rodovia em Dois Irmãos, a 16 km do local do crime. Polícia Civil investiga a motivação para o assassinato](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Presidência da Câmara de Porto Alegre vai propor 'revogaço' de lei que tornou 8 de janeiro o 'Dia do Patriota'. De acordo com o Legislativo, entendimento pelo 'revogaço' se deu a partir da repercussão que o tema teve nos últimos dias. Data é a mesma em que ocorreram atos antidemocráticos em Brasília](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Preso suspeito de sequestrar motorista filmado pedindo socorro de dentro do porta-malas de carro em Porto Alegre. Crime aconteceu em maio deste ano. Motorista de aplicativo foi sequestrado após corrida até Viamão, na Região Metropolitana](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Passagem de meteoro deixa rastro de luz no céu sobre Mostardas. Fenômeno foi registrado na noite de domingo (27). \"Fireball\", como são chamados, recebem esse nome por serem como \"bolas de fogo\": com brilho forte e serem fragmentos de um cometa ou asteroide maior](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n",
        "image_prompt": "\"A stunning, photorealistic illustration of the vibrant and diverse events in Rio Grande do Sul; from the opening of university registrations to the frosty mornings, from the tragic crime to the political turmoil, and from the meteor's trail in the sky to the celebration of Patriot's Day, all captured in a single, breathtaking image.\"",
        "images": [
            "https://drive.google.com/uc?export=view&id=1IG-VmMKXPPDCACrCbnYo5Fu-VNKv8Ux7",
            "https://drive.google.com/uc?export=view&id=1x3CO30iQtoZJPXArBIoorsxQSQMWcJlq",
            "https://drive.google.com/uc?export=view&id=1TPQVHHIZPCbMErdkdbsiYtljqtMPcLQx",
            "https://drive.google.com/uc?export=view&id=1MiE9ZMLRFHs-s4dHjw4u5JztC_lLWXEG"
        ],
        "thumbnails": [
            "https://drive.google.com/uc?export=view&id=1DqtvH_HFhlOnwJld0c657AJbGXrhuOqN",
            "https://drive.google.com/uc?export=view&id=1LmMy_sVw4yCckRXA49hot-8Gx9j8kxr6",
            "https://drive.google.com/uc?export=view&id=1QCVxpMjc0-_DbvQHwJexsEAugM7y5kGu",
            "https://drive.google.com/uc?export=view&id=1z9qanlGPbJKkrX_mEzAQ_VQUZvCpc1ra"
        ]
    }
];

// Call the function
populateGallery(data);
