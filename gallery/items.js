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
        "day_str": "26/08/2023",
        "region": "Porto Alegre",
        "news": "Desculpe-me pela minha resposta anterior. Eu fiz uma pesquisa com a sua pergunta e n\u00e3o encontrei nenhum resumo de not\u00edcias para o dia 26/08/2023 do Rio Grande do Sul e da regi\u00e3o de Porto Alegre. Eu sugiro que voc\u00ea verifique os sites de not\u00edcias locais para obter as \u00faltimas not\u00edcias. Se voc\u00ea tiver alguma outra pergunta ou precisar de ajuda com algo mais, por favor me avise.",
        "news_source": null,
        "image_prompt": "\"A vibrant and detailed illustration of the latest news from Rio Grande do Sul and Porto Alegre, featuring a horse race at the Hip\u00f3dromo do Cristal, a woman receiving medical attention from a bot\u00e3o de emerg\u00eancia in Santa Maria, and the C\u00e2mara de Vereadores de Porto Alegre promulgating a new law.\"",
        "images": [
            "https://drive.google.com/uc?export=view&id=1unT1Xluf3h8ZkhUCTgxHWmbyuJgxIV5s",
            "https://drive.google.com/uc?export=view&id=1WO-gXEhIp30_9ajRTTCfD0m-x60iGemb",
            "https://drive.google.com/uc?export=view&id=13891TUG1o20Ue0NeaCfylWXZ4ouxgNEN",
            "https://drive.google.com/uc?export=view&id=1GtmpyRflCfaIE2NQdwydn2VjOmEtCrIF"
        ]
    },{
        "day_str": "26/08/2023",
        "region": "FAKE POA",
        "news": "Desculpe-me pela minha resposta anterior. Eu fiz uma pesquisa com a sua pergunta e n\u00e3o encontrei nenhum resumo de not\u00edcias para o dia 26/08/2023 do Rio Grande do Sul e da regi\u00e3o de Porto Alegre. Eu sugiro que voc\u00ea verifique os sites de not\u00edcias locais para obter as \u00faltimas not\u00edcias. Se voc\u00ea tiver alguma outra pergunta ou precisar de ajuda com algo mais, por favor me avise.",
        "news_source": null,
        "image_prompt": "\"A vibrant and detailed illustration of the latest news from Rio Grande do Sul and Porto Alegre, featuring a horse race at the Hip\u00f3dromo do Cristal, a woman receiving medical attention from a bot\u00e3o de emerg\u00eancia in Santa Maria, and the C\u00e2mara de Vereadores de Porto Alegre promulgating a new law.\"",
        "images": [
            "https://drive.google.com/uc?export=view&id=1unT1Xluf3h8ZkhUCTgxHWmbyuJgxIV5s",
            "https://drive.google.com/uc?export=view&id=1WO-gXEhIp30_9ajRTTCfD0m-x60iGemb",
            "https://drive.google.com/uc?export=view&id=13891TUG1o20Ue0NeaCfylWXZ4ouxgNEN",
            "https://drive.google.com/uc?export=view&id=1GtmpyRflCfaIE2NQdwydn2VjOmEtCrIF"
        ]
    },
    {
        "day_str": "26/08/2023",
        "region": "Viam\u00c3\u00a3o",
        "news": "Desculpe-me, mas n\u00e3o encontrei nenhuma not\u00edcia que corresponda exatamente ao que voc\u00ea est\u00e1 procurando. No entanto, posso lhe fornecer algumas informa\u00e7\u00f5es gerais sobre as not\u00edcias do dia 26/08/2023 no Rio Grande do Sul e na regi\u00e3o de Viam\u00e3o.\n\nDe acordo com o site Agora RS, uma mulher foi morta a tiros no bairro \u00cdndio Jari em Viam\u00e3o[^4^]. Al\u00e9m disso, o estado do Rio Grande do Sul teve uma nova passagem de ciclone[^5^]. O G1 Rio Grande do Sul relata que o subcomandante de um batalh\u00e3o da BM foi denunciado pelo Minist\u00e9rio P\u00fablico por furto de picanha em supermercado no RS[^3^]. O Jornal NH informa que a Defesa Civil alertou para o risco de temporais no Vale do Sinos e outras regi\u00f5es do RS[^2^].\n\nEspero que essas informa\u00e7\u00f5es ajudem!",
        "news_source": null,
        "image_prompt": "\"A detailed illustration of a woman in Viam\u00e3o caught in a storm while a man steals meat from a supermarket and a cyclone passes by.\"",
        "images": [
            "https://drive.google.com/uc?export=view&id=1JMC0Bs6_xgyjUlgRJMy1aGURRtRbUK6l",
            "https://drive.google.com/uc?export=view&id=1UMzatkc_K9HWKIEIIjgELxa_xwqbVIq1",
            "https://drive.google.com/uc?export=view&id=1vDCGoVXVosZvt41Et3zAn6O8cc_PwDwb",
            "https://drive.google.com/uc?export=view&id=18HccRC15sbn79GjYuKFMr5QsDA5wD6bs"
        ]
    }
]

// Call the function
populateGallery(data);