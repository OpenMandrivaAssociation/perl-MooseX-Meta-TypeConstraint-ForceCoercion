%define module   MooseX-Meta-TypeConstraint-ForceCoercion
%define version  0.01
%define release  %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    No summary found
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/MooseX/%{module}-%{version}.tar.gz
BuildRequires: perl(Moose)
BuildRequires: perl-namespace-autoclean
BuildRequires: perl-namespace-clean
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This class allows to wrap any 'Moose::Meta::TypeConstraint' in a way that
will force coercion of the value when checking or validating a value
against it.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


