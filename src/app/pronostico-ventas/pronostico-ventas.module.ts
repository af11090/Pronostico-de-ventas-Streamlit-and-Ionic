import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { PronosticoVentasPageRoutingModule } from './pronostico-ventas-routing.module';

import { PronosticoVentasPage } from './pronostico-ventas.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    PronosticoVentasPageRoutingModule
  ],
  declarations: [PronosticoVentasPage]
})
export class PronosticoVentasPageModule {}
