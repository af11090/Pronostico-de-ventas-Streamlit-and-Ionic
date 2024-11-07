import { ComponentFixture, TestBed } from '@angular/core/testing';
import { PronosticoVentasPage } from './pronostico-ventas.page';

describe('PronosticoVentasPage', () => {
  let component: PronosticoVentasPage;
  let fixture: ComponentFixture<PronosticoVentasPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(PronosticoVentasPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
