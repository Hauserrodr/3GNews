function populateGallery(data) {
    const container = document.querySelector(".gallery-item");
    
    data.forEach(item => {
        const userContainer = document.createElement('div');
        userContainer.className = 'user-container';
        
        item.images.forEach(imgSrc => {
            console.log(imgSrc)
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
        "day_str": "21/08/2023",
        "headline": "\"Rio Grande do Sul: Vestibular, geada, crime e pol\u00edtica marcam as not\u00edcias do dia\"",
        "region": "Porto Alegre",
        "news": "- [UFRGS abre inscri\u00e7\u00f5es para o Vestibular 2024; saiba mais](^1^)\n- [RS tem manh\u00e3 com geada e temperaturas negativas; Bom Jesus registrou -4\u00baC](^1^)\n- [Jovem \u00e9 executado com tiro durante festa rave em Est\u00e2ncia Velha, diz pol\u00edcia](^1^)\n- [Cuidados desde o nascimento, alimenta\u00e7\u00e3o tr\u00eas vezes ao dia e caminhadas: conhe\u00e7a a rotina do touro mais pesado da Expointer](^1^)\n- [Presid\u00eancia da C\u00e2mara de Porto Alegre vai propor 'revoga\u00e7o' de lei que tornou 8 de janeiro o 'Dia do Patriota'](^1^)\n- [Preso suspeito de sequestrar motorista filmado pedindo socorro de dentro do porta-malas de carro em Porto Alegre](^1^)\n- [Passagem de meteoro deixa rastro de luz no c\u00e9u sobre Mostardas](^1^)\n- [Pol\u00edcia investiga suspeita de golpe em prefeituras do RS ap\u00f3s furto de mais de R$ 1 milh\u00e3o em contas banc\u00e1rias](^2^)",
        "news_source": "[1]: https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/ \"\"\n[2]: https://g1.globo.com/rs/rio-grande-do-sul/noticia/2023/08/27/policia-investiga-suspeita-de-golpe-em-prefeituras-do-rs-apos-furto-de-mais-de-r-1-milhao-em-contas-bancarias.ghtml \"\"\n[3]: https://noticias.uol.com.br/rio-grande-do-sul/noticias/ \"\"\n[4]: https://gauchazh.clicrbs.com.br/ultimas-noticias/tag/rio-grande-do-sul/ \"\"\n[5]: https://agoranors.com/tempo/ \"\"\n\n- [UFRGS abre inscri\u00e7\u00f5es para o Vestibular 2024; saiba mais](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/)\n- [RS tem manh\u00e3 com geada e temperaturas negativas; Bom Jesus registrou -4\u00baC](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/)\n- [Jovem \u00e9 executado com tiro durante festa rave em Est\u00e2ncia Velha, diz pol\u00edcia](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/)\n- [Cuidados desde o nascimento, alimenta\u00e7\u00e3o tr\u00eas vezes ao dia e caminhadas: conhe\u00e7a a rotina do touro mais pesado da Expointer](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/)\n- [Presid\u00eancia da C\u00e2mara de Porto Alegre vai propor 'revoga\u00e7o' de lei que tornou 8 de janeiro o 'Dia do Patriota'](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/)\n- [Preso suspeito de sequestrar motorista filmado pedindo socorro de dentro do porta-malas de carro em Porto Alegre](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/)\n- [Passagem de meteoro deixa rastro de luz no c\u00e9u sobre Mostardas](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/)\n- [Pol\u00edcia investiga suspeita de golpe em prefeituras do RS ap\u00f3s furto de mais de R$ 1 milh\u00e3o em contas banc\u00e1rias](https://g1.globo.com/rs/rio-grande-do-sul/noticia/2023/08/27/policia-investiga-suspeita-de-golpe-em-prefeituras-do-rs-apos-furto-de-mais-de-r-1-milhao-em-contas-bancarias.ghtml) \n",
        "image_prompt": "\"A vivid illustration of daily life in Rio Grande do Sul, capturing its news and events; scenes depicting the opening of UFRGS Vestibular, a frosty morning, a crime scene at a rave party, the routine of the heaviest bull at Expointer, political discussions at the City Council of Porto Alegre, a police operation to arrest a kidnapping suspect, a meteor trail over Mostardas and an investigation into a suspected scam in city halls.\"",
        "images": [
            "https://drive.google.com/uc?export=view&id=164FUTG992nAv6t6H2GgLrRmyw5yZayoA",
            "https://drive.google.com/uc?export=view&id=1UH0QakXa-dqTOTedKbXoSzLD0kn9lcCQ",
            "https://drive.google.com/uc?export=view&id=1NE1O-YnBGHjKx1MAo7AGnbuykNrbIVYw",
            "https://drive.google.com/uc?export=view&id=1aDEHb5StaTUr1MZjHsFWxz8M_HSGQhru"
        ],
        "thumbnails": [
            "https://drive.google.com/uc?export=view&id=1zvzQmOgi6aMEr1O_Z69VTfRDAjWJQPDg",
            "https://drive.google.com/uc?export=view&id=1_LkUImERVAAT3ruz4Ib5-IF3ScEJGDzy",
            "https://drive.google.com/uc?export=view&id=1T5HeojChRUAMNEdI6wnEDefp-CRqLNN2",
            "https://drive.google.com/uc?export=view&id=15jAEo8D7KeP4GKVfeHPhKfp-qKB3ivDw"
        ]
    },
    {
        "day_str": "21/08/2023",
        "headline": "\"Rio Grande do Sul: Inscri\u00e7\u00f5es para o Vestibular 2024 da UFRGS, geada e temperaturas negativas, jovem executado em festa rave, revoga\u00e7o de lei, suspeito preso por sequestro e meteoro no c\u00e9u\"",
        "region": "Viam\u00c3\u00a3o",
        "news": "[Inscri\u00e7\u00f5es para o Vestibular 2024 da UFRGS est\u00e3o abertas at\u00e9 o dia 25 de setembro. A universidade oferece 4.023 vagas de ingresso nos cursos de gradua\u00e7\u00e3o](^1^).\n[Rio Grande do Sul tem manh\u00e3 com geada e temperaturas negativas; Bom Jesus registrou -4\u00baC. De acordo com a Climatempo, condi\u00e7\u00e3o clim\u00e1tica deve se estender at\u00e9 ter\u00e7a (29)](^1^).\n[Jovem \u00e9 executado com tiro durante festa rave em Est\u00e2ncia Velha, diz pol\u00edcia. Corpo foi localizado \u00e0s margens de uma rodovia em Dois Irm\u00e3os, a 16 km do local do crime. Pol\u00edcia Civil investiga a motiva\u00e7\u00e3o para o assassinato](^1^).\n[Presid\u00eancia da C\u00e2mara de Porto Alegre vai propor 'revoga\u00e7o' de lei que tornou 8 de janeiro o 'Dia do Patriota'. De acordo com o Legislativo, entendimento pelo 'revoga\u00e7o' se deu a partir da repercuss\u00e3o que o tema teve nos \u00faltimos dias. Data \u00e9 a mesma em que ocorreram atos antidemocr\u00e1ticos em Bras\u00edlia](^1^).\n[Preso suspeito de sequestrar motorista filmado pedindo socorro de dentro do porta-malas de carro em Porto Alegre. Crime aconteceu em maio deste ano. Motorista de aplicativo foi sequestrado ap\u00f3s corrida at\u00e9 Viam\u00e3o, na Regi\u00e3o Metropolitana](^1^).\n[Passagem de meteoro deixa rastro de luz no c\u00e9u sobre Mostardas. Fen\u00f4meno foi registrado na noite de domingo (27). \"Fireball\", como s\u00e3o chamados, recebem esse nome por serem como \"bolas de fogo\": com brilho forte e serem fragmentos de um cometa ou asteroide maior](^1^).",
        "news_source": "[1]: https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/ \"\"\n[2]: https://g1.globo.com/rs/rio-grande-do-sul/ \"\"\n[3]: https://noticias.uol.com.br/rio-grande-do-sul/noticias/ \"\"\n[4]: https://gauchazh.clicrbs.com.br/ultimas-noticias/tag/rio-grande-do-sul/ \"\"\n[5]: https://www.cnnbrasil.com.br/tudo-sobre/rio-grande-do-sul/ \"\"\n\n[Inscri\u00e7\u00f5es para o Vestibular 2024 da UFRGS est\u00e3o abertas at\u00e9 o dia 25 de setembro. A universidade oferece 4.023 vagas de ingresso nos cursos de gradua\u00e7\u00e3o](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Rio Grande do Sul tem manh\u00e3 com geada e temperaturas negativas; Bom Jesus registrou -4\u00baC. De acordo com a Climatempo, condi\u00e7\u00e3o clim\u00e1tica deve se estender at\u00e9 ter\u00e7a (29)](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Jovem \u00e9 executado com tiro durante festa rave em Est\u00e2ncia Velha, diz pol\u00edcia. Corpo foi localizado \u00e0s margens de uma rodovia em Dois Irm\u00e3os, a 16 km do local do crime. Pol\u00edcia Civil investiga a motiva\u00e7\u00e3o para o assassinato](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Presid\u00eancia da C\u00e2mara de Porto Alegre vai propor 'revoga\u00e7o' de lei que tornou 8 de janeiro o 'Dia do Patriota'. De acordo com o Legislativo, entendimento pelo 'revoga\u00e7o' se deu a partir da repercuss\u00e3o que o tema teve nos \u00faltimos dias. Data \u00e9 a mesma em que ocorreram atos antidemocr\u00e1ticos em Bras\u00edlia](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Preso suspeito de sequestrar motorista filmado pedindo socorro de dentro do porta-malas de carro em Porto Alegre. Crime aconteceu em maio deste ano. Motorista de aplicativo foi sequestrado ap\u00f3s corrida at\u00e9 Viam\u00e3o, na Regi\u00e3o Metropolitana](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Passagem de meteoro deixa rastro de luz no c\u00e9u sobre Mostardas. Fen\u00f4meno foi registrado na noite de domingo (27). \"Fireball\", como s\u00e3o chamados, recebem esse nome por serem como \"bolas de fogo\": com brilho forte e serem fragmentos de um cometa ou asteroide maior](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n",
        "image_prompt": "\"A stunning, photorealistic illustration of the latest news from Rio Grande do Sul, Brazil; a vibrant, detailed composition featuring the UFRGS Vestibular 2024, frost and negative temperatures, a young man executed at a rave party, the revocation of a law, a suspect arrested for kidnapping, and a meteor in the sky.\"",
        "images": [
            "https://drive.google.com/uc?export=view&id=1ofioudwo45IJebPoYPcdBdD7DBXQdYfi",
            "https://drive.google.com/uc?export=view&id=1OhyvTf5Z5b-C5jwTqfjKpEqECmHandZz",
            "https://drive.google.com/uc?export=view&id=1UUIVl5Pd1woNe-FHTAMLT-_hZXZw0hJO",
            "https://drive.google.com/uc?export=view&id=1GuiePFWkOiFSwpRhE0NF8LPA18IIbv-N"
        ],
        "thumbnails": [
            "https://drive.google.com/uc?export=view&id=1d8vsmR3iptMEv-d1IAAQ_KmgUC4GfY4B",
            "https://drive.google.com/uc?export=view&id=1AcEhAHLa1Btmd5j7jWHO_PxltMpqJ21J",
            "https://drive.google.com/uc?export=view&id=1HXSeBqtNee71GJ9aEdoTdwT5KiuS9OyE",
            "https://drive.google.com/uc?export=view&id=15WDUPD79hrasFQOzYNnlrH_Ox-7olpiX"
        ]
    },
    {
        "day_str": "29/08/2023",
        "headline": "\"Rio Grande do Sul: Inscri\u00e7\u00f5es para o Vestibular da UFRGS, geada e temperaturas negativas, execu\u00e7\u00e3o em festa rave, revoga\u00e7o de lei, suspeita de golpe contra prefeituras, acidente de carro, rastro de fogo de lixo espacial e queda no n\u00famero de registros de armas de fogo\"",
        "region": "Porto Alegre",
        "news": "[As inscri\u00e7\u00f5es para o Vestibular 2024 da UFRGS est\u00e3o abertas at\u00e9 as 23h59 do dia 25 de setembro. A universidade oferece 4.023 vagas de ingresso nos cursos de gradua\u00e7\u00e3o](^1^).\n[Rio Grande do Sul teve uma manh\u00e3 com geada e temperaturas negativas, Bom Jesus registrou -4\u00baC. De acordo com a Climatempo, a condi\u00e7\u00e3o clim\u00e1tica deve se estender at\u00e9 ter\u00e7a (29)](^1^).\n[Um jovem foi executado com um tiro durante uma festa rave em Est\u00e2ncia Velha, a pol\u00edcia est\u00e1 investigando a motiva\u00e7\u00e3o para o assassinato](^1^).\n[A presid\u00eancia da C\u00e2mara de Porto Alegre vai propor 'revoga\u00e7o' de lei que tornou 8 de janeiro o 'Dia do Patriota'](^1^).\n[A Pol\u00edcia Civil est\u00e1 investigando uma suspeita de golpe contra quatro prefeituras do Rio Grande do Sul. Segundo as investiga\u00e7\u00f5es, os munic\u00edpios perderam, ao todo, quase R$1,5 milh\u00e3o durante ataques eletr\u00f4nicos nas \u00faltimas semanas](^2^).\n[Um carro n\u00e3o parou e caiu em um rio, uma mulher morreu no Rio Grande do Sul](^3^).\n[Rastro de fogo de lixo espacial foi registrado em cidades do RS](^3^).\n[\u00c9 impressionante a queda no n\u00famero de novos registros de armas de fogo no RS](^4^).\n[Nuvens carregadas est\u00e3o provocando temporais isolados pelo Rio Grande do Sul. Segundo a previs\u00e3o do tempo, o avan\u00e7o de uma massa de ar frio provoca o decl\u00ednio nas temperaturas](^5^).",
        "news_source": "[1]: https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/ \"\"\n[2]: https://g1.globo.com/rs/rio-grande-do-sul/noticia/2023/08/27/policia-investiga-suspeita-de-golpe-em-prefeituras-do-rs-apos-furto-de-mais-de-r-1-milhao-em-contas-bancarias.ghtml \"\"\n[3]: https://noticias.uol.com.br/rio-grande-do-sul/noticias/ \"\"\n[4]: https://gauchazh.clicrbs.com.br/ultimas-noticias/tag/rio-grande-do-sul/ \"\"\n[5]: https://agoranors.com/tempo/ \"\"\n\n[As inscri\u00e7\u00f5es para o Vestibular 2024 da UFRGS est\u00e3o abertas at\u00e9 as 23h59 do dia 25 de setembro. A universidade oferece 4.023 vagas de ingresso nos cursos de gradua\u00e7\u00e3o](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Rio Grande do Sul teve uma manh\u00e3 com geada e temperaturas negativas, Bom Jesus registrou -4\u00baC. De acordo com a Climatempo, a condi\u00e7\u00e3o clim\u00e1tica deve se estender at\u00e9 ter\u00e7a (29)](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Um jovem foi executado com um tiro durante uma festa rave em Est\u00e2ncia Velha, a pol\u00edcia est\u00e1 investigando a motiva\u00e7\u00e3o para o assassinato](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[A presid\u00eancia da C\u00e2mara de Porto Alegre vai propor 'revoga\u00e7o' de lei que tornou 8 de janeiro o 'Dia do Patriota'](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[A Pol\u00edcia Civil est\u00e1 investigando uma suspeita de golpe contra quatro prefeituras do Rio Grande do Sul. Segundo as investiga\u00e7\u00f5es, os munic\u00edpios perderam, ao todo, quase R$1,5 milh\u00e3o durante ataques eletr\u00f4nicos nas \u00faltimas semanas](https://g1.globo.com/rs/rio-grande-do-sul/noticia/2023/08/27/policia-investiga-suspeita-de-golpe-em-prefeituras-do-rs-apos-furto-de-mais-de-r-1-milhao-em-contas-bancarias.ghtml).\n[Um carro n\u00e3o parou e caiu em um rio, uma mulher morreu no Rio Grande do Sul](https://noticias.uol.com.br/rio-grande-do-sul/noticias/).\n[Rastro de fogo de lixo espacial foi registrado em cidades do RS](https://noticias.uol.com.br/rio-grande-do-sul/noticias/).\n[\u00c9 impressionante a queda no n\u00famero de novos registros de armas de fogo no RS](https://gauchazh.clicrbs.com.br/ultimas-noticias/tag/rio-grande-do-sul/).\n[Nuvens carregadas est\u00e3o provocando temporais isolados pelo Rio Grande do Sul. Segundo a previs\u00e3o do tempo, o avan\u00e7o de uma massa de ar frio provoca o decl\u00ednio nas temperaturas](https://agoranors.com/tempo/).",
        "image_prompt": "\"A vivid, detailed illustration of the latest news from Rio Grande do Sul, Brazil; a collage of events including the opening of UFRGS Vestibular registrations, frost and negative temperatures, execution at a rave party, revocation of law, suspicion of fraud against city halls, car accident, trail of space debris fire and drop in the number of firearm registrations.\"",
        "images": [
            "https://drive.google.com/uc?export=view&id=1OX6lp3b_Tt2CE7plf9Cmfie_8NUZwmmU",
            "https://drive.google.com/uc?export=view&id=1G4yQnkXi2e5Vi9Ow5W1EqwT0EN6kfA7f",
            "https://drive.google.com/uc?export=view&id=14BN3PStinv7R1wwQ67EW0aW-Q5aqMF_K",
            "https://drive.google.com/uc?export=view&id=1Li7UL21YvFwZ9Yd2YRx6eGEfpgMhjehL"
        ],
        "thumbnails": [
            "https://drive.google.com/uc?export=view&id=1fIkQcbmRHoJkRL_T2lCPlaAp5Yr2MwAX",
            "https://drive.google.com/uc?export=view&id=1RB96zr3TYYSKwa1l97v12fy81WQUmHY2",
            "https://drive.google.com/uc?export=view&id=11WLipC-T-fpB5G4hMbMrWa5nIrKuiuAj",
            "https://drive.google.com/uc?export=view&id=1sG6cTrG957PtRhqHeKzzWlDV6gagndiD"
        ]
    },
    {
        "day_str": "29/08/2023",
        "headline": "\"Rio Grande do Sul: Vestibular, geada, crime, pol\u00edtica e fen\u00f4meno no c\u00e9u marcam a semana\"",
        "region": "Viam\u00c3\u00a3o",
        "news": "[Universidade Federal do Rio Grande do Sul (UFRGS) abre inscri\u00e7\u00f5es para o Vestibular 2024 at\u00e9 as 23h59 do dia 25 de setembro, oferecendo 4.023 vagas de ingresso nos cursos de gradua\u00e7\u00e3o](^1^).\n[Rio Grande do Sul tem manh\u00e3 com geada e temperaturas negativas; Bom Jesus registrou -4\u00baC. De acordo com a Climatempo, condi\u00e7\u00e3o clim\u00e1tica deve se estender at\u00e9 ter\u00e7a (29)](^1^).\n[Jovem \u00e9 executado com tiro durante festa rave em Est\u00e2ncia Velha, diz pol\u00edcia. Corpo foi localizado \u00e0s margens de uma rodovia em Dois Irm\u00e3os, a 16 km do local do crime. Pol\u00edcia Civil investiga a motiva\u00e7\u00e3o para o assassinato](^1^).\n[Presid\u00eancia da C\u00e2mara de Porto Alegre vai propor 'revoga\u00e7o' de lei que tornou 8 de janeiro o 'Dia do Patriota'. De acordo com o Legislativo, entendimento pelo 'revoga\u00e7o' se deu a partir da repercuss\u00e3o que o tema teve nos \u00faltimos dias. Data \u00e9 a mesma em que ocorreram atos antidemocr\u00e1ticos em Bras\u00edlia](^1^).\n[Preso suspeito de sequestrar motorista filmado pedindo socorro de dentro do porta-malas de carro em Porto Alegre. Crime aconteceu em maio deste ano. Motorista de aplicativo foi sequestrado ap\u00f3s corrida at\u00e9 Viam\u00e3o, na Regi\u00e3o Metropolitana](^1^).\n[Passagem de meteoro deixa rastro de luz no c\u00e9u sobre Mostardas. Fen\u00f4meno foi registrado na noite de domingo (27). \"Fireball\", como s\u00e3o chamados, recebem esse nome por serem como \"bolas de fogo\": com brilho forte e serem fragmentos de um cometa ou asteroide maior](^1^).",
        "news_source": "[1]: https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/ \"\"\n[2]: https://g1.globo.com/rs/rio-grande-do-sul/ \"\"\n[3]: https://noticias.uol.com.br/rio-grande-do-sul/noticias/ \"\"\n[4]: https://gauchazh.clicrbs.com.br/ultimas-noticias/tag/rio-grande-do-sul/ \"\"\n[5]: https://www.cnnbrasil.com.br/tudo-sobre/rio-grande-do-sul/ \"\"\n\n[Universidade Federal do Rio Grande do Sul (UFRGS) abre inscri\u00e7\u00f5es para o Vestibular 2024 at\u00e9 as 23h59 do dia 25 de setembro, oferecendo 4.023 vagas de ingresso nos cursos de gradua\u00e7\u00e3o](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Rio Grande do Sul tem manh\u00e3 com geada e temperaturas negativas; Bom Jesus registrou -4\u00baC. De acordo com a Climatempo, condi\u00e7\u00e3o clim\u00e1tica deve se estender at\u00e9 ter\u00e7a (29)](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Jovem \u00e9 executado com tiro durante festa rave em Est\u00e2ncia Velha, diz pol\u00edcia. Corpo foi localizado \u00e0s margens de uma rodovia em Dois Irm\u00e3os, a 16 km do local do crime. Pol\u00edcia Civil investiga a motiva\u00e7\u00e3o para o assassinato](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Presid\u00eancia da C\u00e2mara de Porto Alegre vai propor 'revoga\u00e7o' de lei que tornou 8 de janeiro o 'Dia do Patriota'. De acordo com o Legislativo, entendimento pelo 'revoga\u00e7o' se deu a partir da repercuss\u00e3o que o tema teve nos \u00faltimos dias. Data \u00e9 a mesma em que ocorreram atos antidemocr\u00e1ticos em Bras\u00edlia](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Preso suspeito de sequestrar motorista filmado pedindo socorro de dentro do porta-malas de carro em Porto Alegre. Crime aconteceu em maio deste ano. Motorista de aplicativo foi sequestrado ap\u00f3s corrida at\u00e9 Viam\u00e3o, na Regi\u00e3o Metropolitana](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n[Passagem de meteoro deixa rastro de luz no c\u00e9u sobre Mostardas. Fen\u00f4meno foi registrado na noite de domingo (27). \"Fireball\", como s\u00e3o chamados, recebem esse nome por serem como \"bolas de fogo\": com brilho forte e serem fragmentos de um cometa ou asteroide maior](https://g1.globo.com/rs/rio-grande-do-sul/ultimas-noticias/).\n",
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
]
// Call the function
populateGallery(data);