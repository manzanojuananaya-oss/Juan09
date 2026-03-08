<!doctype html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Para Yexa </title>
  <style>
    :root{
      --bg1:#fff5fb;
      --bg2:#f4e8ff;
      --bg3:#ffe1f1;
      --card:#ffffffcc;
      --text:#3f2f46;

      --pink:#ff5ca8;
      --lila:#b57cff;
      --morado:#8b4dff;
      --hoja:#57b56f;
      --tallo:#3f9e59;
    }

    *{box-sizing:border-box}
    body{
      margin:0;
      min-height:100vh;
      font-family: "Segoe UI", Tahoma, sans-serif;
      color:var(--text);
      background:
        radial-gradient(circle at 10% 10%, #ffffffaa 0%, transparent 35%),
        radial-gradient(circle at 90% 20%, #ffffff99 0%, transparent 30%),
        linear-gradient(130deg,var(--bg1),var(--bg2),var(--bg3));
      overflow-x:hidden;
    }

    .wrap{
      width:min(1200px,94vw);
      margin:34px auto;
      display:grid;
      gap:22px;
    }

    .hero, .panel{
      background:var(--card);
      border:1px solid #f3c8ff;
      border-radius:24px;
      box-shadow:0 16px 40px rgba(95,52,121,.15);
      backdrop-filter: blur(6px);
    }

    .hero{
      text-align:center;
      padding:30px 24px;
    }
    .hero h1{
      margin:0;
      font-size:clamp(2rem,5vw,3.4rem);
      color:#b23cff;
      letter-spacing:.4px;
    }
    .hero p{
      max-width:760px;
      margin:10px auto 0;
      line-height:1.8;
      font-size:1.08rem;
    }

    .grid{
      display:grid;
      grid-template-columns:1fr 1fr;
      gap:22px;
    }

    .panel{
      padding:20px;
    }

    .panel h2{
      margin:0 0 14px;
      color:#a32ddf;
      font-size:1.4rem;
    }

    .dedica p{
      margin:.35rem 0;
      line-height:1.85;
      font-size:1.05rem;
    }

    .firma{
      margin-top:12px;
      font-weight:700;
      color:#c22484;
    }

    .garden{
      position:relative;
      min-height:560px;
      border-radius:20px;
      padding:14px 8px 20px;
      background:
        linear-gradient(to top, #e2ffe9 0 18%, transparent 18%),
        radial-gradient(circle at 50% 110%, #a6f0b8 0 20%, transparent 21%);
      display:grid;
      grid-template-columns:repeat(4,minmax(120px,1fr));
      align-items:end;
      justify-items:center;
      gap:10px;
    }

    .tulip{
      position:relative;
      width:120px;
      height:280px;
      transform-origin:bottom center;
      animation:sway 3.2s ease-in-out infinite;
      filter:drop-shadow(0 8px 6px rgba(0,0,0,.09));
    }
    .tulip:nth-child(2n){animation-delay:.3s}
    .tulip:nth-child(3n){animation-delay:.6s}
    .tulip:nth-child(4n){animation-delay:.9s}

    .stem{
      position:absolute;
      left:50%;
      bottom:0;
      transform:translateX(-50%);
      width:10px;
      height:180px;
      background:linear-gradient(var(--hoja),var(--tallo));
      border-radius:10px;
    }

    .leaf{
      position:absolute;
      bottom:78px;
      width:40px;
      height:18px;
      background:linear-gradient(90deg,#79d68f,#4ea964);
    }
    .leaf.left{
      left:20px;
      border-radius:20px 20px 20px 2px;
      transform:rotate(-28deg);
    }
    .leaf.right{
      right:20px;
      border-radius:20px 20px 2px 20px;
      transform:rotate(28deg);
    }

    .flower{
      position:absolute;
      left:50%;
      top:20px;
      transform:translateX(-50%);
      width:90px;
      height:95px;
    }

    .petal{
      position:absolute;
      width:42px;
      height:64px;
      border-radius:26px 26px 14px 14px;
      box-shadow: inset 0 10px 12px #ffffff55;
    }

    .petal.c{ left:24px; top:8px; z-index:3; }
    .petal.l{ left:6px; top:14px; transform:rotate(-16deg); z-index:2;}
    .petal.r{ left:42px; top:14px; transform:rotate(16deg); z-index:2;}

    .pink .petal.c{background:#ff4fa1}
    .pink .petal.l,.pink .petal.r{background:#ff85bf}

    .lila .petal.c{background:#b87dff}
    .lila .petal.l,.lila .petal.r{background:#ceabff}

    .morado .petal.c{background:#8d4eff}
    .morado .petal.l,.morado .petal.r{background:#a976ff}

    .controls{
      margin-top:16px;
      display:flex;
      gap:10px;
      flex-wrap:wrap;
    }

    button{
      border:none;
      border-radius:999px;
      padding:10px 16px;
      font-weight:700;
      cursor:pointer;
      background:#c046ff;
      color:#fff;
    }
    button:hover{filter:brightness(.95)}

    .msg{
      min-height:30px;
      margin-top:10px;
      color:#9b1cc8;
      font-weight:700;
    }

    @keyframes sway{
      0%,100%{transform:rotate(-1.5deg)}
      50%{transform:rotate(1.5deg)}
    }

    @media (max-width:900px){
      .grid{grid-template-columns:1fr}
      .garden{grid-template-columns:repeat(3,minmax(100px,1fr)); min-height:500px}
      .tulip{width:105px;height:250px}
      .stem{height:165px}
    }

    @media (max-width:560px){
      .garden{grid-template-columns:repeat(2,minmax(100px,1fr))}
    }
  </style>
</head>
<body>
  <main class="wrap">
    <section class="hero">
      <h1>Para Yexal </h1>
      <p>
        Hice este jardín 
        Cada flor guarda una palabra bonita que quiero dedicarte.
      </p>
    </section>

    <section class="grid">
      <article class="panel">
        <h2>Dedicatoria</h2>
        <div class="dedica">
          <p>Eres ternura, fuerza y luz en una sola persona.</p>
          <p>Tu sonrisa me calma, tu presencia me inspira.</p>
          <p>Si te pudiera regalar un jardín, sería así: lila, morado y rosa.</p>
          <p>Porque esos colores se quedan cortos para lo especial que eres.</p>
        </div>
        <p class="firma">Con cariño, alguien que te quiere mucho.</p>

        <div class="controls">
          <button id="btnFrase">Mostrar frase bonita</button>
        </div>
        <div class="msg" id="msg"></div>
      </article>

      <aside class="panel">
        <h2>Jardín de tulipanes</h2>
        <div class="garden" id="garden"></div>
      </aside>
    </section>
  </main>

  <script>
    const garden = document.getElementById("garden");
    const frases = [
      "Eres mi color favorito en cualquier día gris.",
      "Contigo, todo se siente más bonito.",
      "Tus ojos tienen paz de primavera.",
      "Siempre voy a querer verte sonreír."
    ];

    const clases = ["pink", "lila", "morado"];

    function tulip(tipo){
      const d = document.createElement("div");
      d.className = `tulip ${tipo}`;
      d.innerHTML = `
        <div class="flower">
          <span class="petal l"></span>
          <span class="petal c"></span>
          <span class="petal r"></span>
        </div>
        <div class="stem"></div>
        <div class="leaf left"></div>
        <div class="leaf right"></div>
      `;
      return d;
    }

    for(let i=0;i<12;i++){
      const t = tulip(clases[i % clases.length]);
      garden.appendChild(t);
    }

    document.getElementById("btnFrase").addEventListener("click", () => {
      const i = Math.floor(Math.random()*frases.length);
      document.getElementById("msg").textContent = frases[i];
    });
  </script>
</body>
</html>
