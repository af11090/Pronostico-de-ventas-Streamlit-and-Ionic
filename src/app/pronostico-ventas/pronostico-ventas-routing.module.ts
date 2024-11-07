import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PronosticoVentasPage } from './pronostico-ventas.page';

const routes: Routes = [
  {
    path: '',
    component: PronosticoVentasPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PronosticoVentasPageRoutingModule {}
