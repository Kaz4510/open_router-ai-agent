## Architecture

```mermaid
flowchart LR
    DB[(Postgres<br/>smdg_terminals)] --> BE
    BE[FastAPI backend<br/>:8000] --> FE
    FE[React + Vite<br/>Mapbox GL<br/>:5173] --> BE
    BE --> FS[(bboxes.parquet<br/>status.json)]
    FS --> PL[Image pipelines<br/>tile / mapbox]
    PL --> OUT[(GeoTIFFs<br/>dataset/*.tiff)]
```


![github_profile](https://avatars.githubusercontent.com/u/60610819?v=4 "user_profile")

# Math Rendering Test
  ## Inline math                                     
  Einstein's mass-energy equivalence: $E = mc^2$. 
  The quadratic formula is 
  $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$, 
  and Euler's identity 
  $e^{i\pi} + 1 =   0$ 
    is famously elegant.                            
                                                     
  ## Display math (block)                            
$$\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}$$                                                 
                                                     
  ## Fractions, sums, products                       
$$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}\qquadprod_{k=1}^{n} k = n!$$



