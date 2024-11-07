import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./tabs/tabs.module').then(m => m.TabsPageModule)
  },
  {
    path: 'pronostico-ventas',
    loadChildren: () => import('./pronostico-ventas/pronostico-ventas.module').then( m => m.PronosticoVentasPageModule)
  },
  {
    path: 'pronostico',
    loadChildren: () => import('./pronostico/pronostico.module').then( m => m.PronosticoPageModule)
  }
];
@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
